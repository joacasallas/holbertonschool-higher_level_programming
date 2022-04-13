#!/usr/bin/node
// searches the second biggest integer in the list of arguments.
let i = 0;
let mayor = 0;
let submayor = 0;
for (; process.argv[i] != null; i++) {
  if (process.argv[i] > mayor) {
    submayor = mayor;
    mayor = process.argv[i];
  } else if (process.argv[i] > submayor) {
    submayor = process.argv[i];
  }
}
if (i === 2 || i === 3) {
  console.log(0);
} else {
  console.log(submayor);
}
