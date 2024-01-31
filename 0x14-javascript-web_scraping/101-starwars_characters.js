#!/usr/bin/node

const request = require('request');

const movie_id = process.argv[2];
const movie_url = `https://swapi.dev/api/films/${movie_id}/`;
let characters = [];

request(movie_url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const json_data = JSON.parse(body);
  characters = json_data.characters;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    getCharacters(index + 1);
  });
};
