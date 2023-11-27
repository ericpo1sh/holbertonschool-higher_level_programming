#!/usr/bin/node
// Write a class Square that defines a square
const oldSquare = require('./5-square');
module.exports = class Square extends oldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let y = 1; y <= this.width; y++) {
      let set = '';
      for (let x = 1; x <= this.width; x++) {
        set += c;
      }
      console.log(set);
    }
  }
};
