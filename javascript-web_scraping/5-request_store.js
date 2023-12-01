#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

async function requestStore (url, file) {
  request.get(url, (error, response, body) => {
    if (error) console.log(error);
    else if (response.statusCode === 404) console.log(`code: ${response.statusCode}`);
    else {
      fs.writeFile(file, (body), 'utf-8', (error) => {
        if (error) {
          console.error(error);
        }
      });
    }
  });
}
requestStore(process.argv[2], process.argv[3]);
