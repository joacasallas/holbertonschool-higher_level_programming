#!/usr/bin/node
//  computes and prints a factorial
function factorial (n) {
  if (isNaN(Number(process.argv[2]))) { 
      return 1;
  }
  if (n > 1) {
    n = n * factorial(n - 1);
  }
  return n;
}
console.log(factorial(Number(process.argv[2])));
