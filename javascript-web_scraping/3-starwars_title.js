#!/usr/bin/node
// Write a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.
const request = require('request');
async function starWarsTitle (id) {
  request.get(`https://swapi-api.hbtn.io/api/films/${id}`, (error, response, body) => {
    if (error) console.log(error);
    else if (response.statusCode === 404) console.log(`code: ${response.statusCode}`);
    else if (body) console.log(JSON.parse(body).title);
  });
}
starWarsTitle(process.argv[2]);
