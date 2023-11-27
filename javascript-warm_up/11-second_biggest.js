#!/usr/bin/node
// Searches the second biggest integer in the list of arguments
if (process.argv.length < 3 || process.argv.length === 3) {
  console.log('0');
} else {
  const array = process.argv.slice(2).sort((b, a) => a - b);
  console.log(array[0]);
}
