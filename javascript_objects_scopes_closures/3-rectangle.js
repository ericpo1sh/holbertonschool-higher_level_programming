#!/usr/bin/node
// Write a class Rectangle that defines a rectangle
// if w or h is equal to 0 or not a positive integer, create an empty object
// Create an instance method called print()
module.exports = class Rectangle {
  constructor (w, h) { // Adding parameters for the class
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let y = 1; y <= this.height; y++) {
      let set = '';
      for (let x = 1; x <= this.width; x++) {
        set += 'X';
      }
      console.log(set);
    }
  }
};
