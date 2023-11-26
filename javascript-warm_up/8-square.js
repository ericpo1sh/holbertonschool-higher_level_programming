#!/usr/bin/node
// Write a script that prints a square
const number = Number(process.argv[2]);
if (process.argv.length === 3) {
  if (number > 0) {
    for (let y = 1; y <= number; y++) {
      let set = '';
      for (let x = 1; x <= number; x++) {
        set += 'X';
      }
      console.log(set);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
