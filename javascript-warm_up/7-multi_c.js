#!/usr/bin/node
// Write a script that prints x times “C is fun”
const number = Number(process.argv[2]);
if (process.argv.length === 3) {
  if (number > 0) {
    for (let x = 1; x <= number; x++) {
      console.log('C is fun');
    }
  }
} else if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
}
