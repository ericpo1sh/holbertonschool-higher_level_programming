#!/usr/bin/node
// Write a function that returns the reversed version of a list:

exports.esrever = function (list) {
  list.sort((a, b) => b - a);
  return list;
};
