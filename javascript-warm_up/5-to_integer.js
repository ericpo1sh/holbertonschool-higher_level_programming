#!/usr/bin/node
// Wtire a script that prints if first arg is a int
// Converting argv[2] into a number
const number = Number(process.argv[2]);
// checking if it is a number
if (!isNaN(number)) {
// remove decimals from the number and print
  const numb = number | 0;
  console.log('My number: ' + numb);
} else {
  console.log('Not a number');
}
