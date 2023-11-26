#!/usr/bin/node
// make a function that adds two parameters
function add (a, b) {
  return a + b;
}
const number1 = Number(process.argv[2]);
const number2 = Number(process.argv[3]);
console.log(add(number1, number2));
