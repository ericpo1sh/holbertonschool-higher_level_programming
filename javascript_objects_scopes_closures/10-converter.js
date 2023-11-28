#!/usr/bin/node
// Function that convers numbers to selected base
exports.converter = function (base) {
  return num => num.toString(base);
};
