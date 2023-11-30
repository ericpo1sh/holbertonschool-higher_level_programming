#!/usr/bin/node
// Write a script that reads and prints the content of a file.

const fs = require('fs');
async function readme (filename) {
  const data = fs.readFile(filename, 'utf-8', (error, data) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log(data.toString());
  });
}
readme(process.argv[2]);
