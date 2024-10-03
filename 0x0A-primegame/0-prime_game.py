#!/usr/bin/python3
"""
This module defines a set of functions that solve a challenge that involves
determining a game winner based on the strategic removal of prime numbers
and their multiples from a set of consecutive integers
"""


def isWinner(x, nums):
    """
    Function determines winner
    Args:
        x - number of rounds
        nums - an array of n
        n - last and included int in a set from 1
    Returns:
           Name of the player that won the most rounds
           None, if winner cannot be determined
    """
    def sieve_of_eratosthenes(n):
        """
         Function generates prime numbers up to max number in nums
        """
        s = [True] * (n + 1)
        s[0] = s[1] = False
        primes = []
        for i in range(2, n + 1):
            if s[i]:
                primes.append(i)
                for m in range(i * i, n + 1, i):
                    s[m] = False
        return primes

    def game_winner(n, primes):
        """
        Helper function, determines the winner for a given round with n numbers
        """
        primes_in_set = [p for p in primes if p <= n]
        ms = 0
        # Count the number of moves (removals) until no primes are left
        for prime in primes_in_set:
            if prime <= n:
                ms += 1
                # Remove the prime and its multiples
                n -= 1
        # Maria wins if the number of moves is odd, Ben wins if even
        return "Maria" if ms % 2 != 0 else "Ben"

    # Find the maximum n in nums to avoid recalculating primes for each round
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Count the wins for each player
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        winner = game_winner(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
