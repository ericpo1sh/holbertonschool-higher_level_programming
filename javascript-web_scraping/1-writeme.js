#!/usr/bin/node
// Write a script that writes a string to a file.

const fs = require('fs');

async function writeme (filename, string) {
  fs.writeFile(filename, string, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    }
  });
}
writeme(process.argv[2], process.argv[3]);
