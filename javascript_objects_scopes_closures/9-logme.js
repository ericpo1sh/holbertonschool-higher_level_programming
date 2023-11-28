#!/usr/bin/node
// function that prints the number of arguments already printed
let count = 0;
exports.logMe = function (item) {
  count++;
  console.log(`${count}: ${item}`);
};
