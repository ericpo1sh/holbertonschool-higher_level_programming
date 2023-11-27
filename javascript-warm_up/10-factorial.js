#!/usr/bin/node
// Writing a scrpt that returns the factorial of input
function factorial (n) {
  if (n < 0) {
    return -1; // return 1 if number is 0-1
  } else if (n === 0 || n === 1) {
    return 1;
  }  {
    return n * factorial(n - 1); // Recursively call factorial function
  }
}
const n = Number(process.argv[2]);
if (isNaN(n)) {
  return;
}
console.log(factorial(n));
