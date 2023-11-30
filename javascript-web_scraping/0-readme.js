#!/usr/bin/node
// Write a script that reads and prints the content of a file.

const fs = require('fs').promises;
async function readme (filename) {
  try {
    const data = await fs.readFile(filename, 'utf-8');
    console.log(data.toString());
  } catch (error) {
    console.error(error);
  }
}
readme(process.argv[2]);
