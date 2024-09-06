#!/usr/bin/node

const request = require('request');

const args = process.argv;
const baseUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieUrl = `${baseUrl}${args[2]}/`;

let charIndex = 0;
let charUrl = [];

function getMovieDets () {
  request(movieUrl, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const movieDets = JSON.parse(body);
      charUrl = movieDets.characters;
      if (charUrl.length > 0) {
        getCharDets();
      }
    } else {
      console.log(error);
    }
  });
}

function getCharDets () { // fetch character details from API
  if (charIndex < charUrl.length) {
    request(charUrl[charIndex], function (error, response, body) {
      if (!error && response.statusCode === 200) {
        const charDets = JSON.parse(body);
        console.log(charDets.name);
        charIndex++;
        getCharDets();
      } else {
        console.error('error:', error);
      }
    });
  }
}

getMovieDets();
