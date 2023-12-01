#!/usr/bin/node
// Write a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.
const request = require('request');
async function starWarsCount (url) {
  request.get(url, (error, response, body) => {
    if (error) console.log(error);
    else if (response.statusCode === 404) console.log(`code: ${response.statusCode}`);
    else if (body) {
      let count = 0;
      const rizzults = JSON.parse(body).results;
      for (const film of rizzults) {
        for (const character of film.characters) {
          if (character.match(/.\/18\//g)) {
            count += 1;
          }
        }
      }
      console.log(count);
    }
  });
}
starWarsCount(process.argv[2]);
