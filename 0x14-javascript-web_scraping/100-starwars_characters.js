#!/usr/bin/node

const request = require('request');

const movie_id = process.argv[2];
const movie_url = `https://swapi.dev/api/films/${movie_id}/`;

request.get(movie_url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const json_data = JSON.parse(body);
  const characters = json_data.characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
