#!/usr/bin/node
// Write a script that display the status code of a GET request.
const request = require('request');
async function getRequest (url) {
  request(url, (error, response) => {
    if (error) console.log(error);
    console.log(`code: ${response.statusCode}`);
  });
}
getRequest(process.argv[2]);
