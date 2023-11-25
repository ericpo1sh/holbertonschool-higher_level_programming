#!/usr/bin/node
// Write a script that prints the arg thats passes
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
