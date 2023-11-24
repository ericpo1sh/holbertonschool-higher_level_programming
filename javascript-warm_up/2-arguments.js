#!/usr/bin/node
// Write a script that prints message when arg passed
if (process.argv.length >= 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
