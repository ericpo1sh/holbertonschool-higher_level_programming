#!/usr/bin/node
// Writing a scrpt that returns the factorial of input
function factorial (number) {
  if (number <=  1) {
    return 1; // return 1 if number is 0-1
  } else {
    return number * factorial(number - 1); // Recursively call factorial function
  }
}
const number = Number(process.argv[2]);
console.log(factorial(number));
