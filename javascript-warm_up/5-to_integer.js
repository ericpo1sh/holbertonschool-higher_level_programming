#!/usr/bin/node
// Wtire a script that prints if first arg is a int
const number = Number(process.argv[2]);
const numb = number | 0;
if (!isNaN(numb)) {
  console.log('My number: ' + numb);
} else {
  console.log('Not a number');
}
