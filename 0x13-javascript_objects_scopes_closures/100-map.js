#!/usr/bin/node
// import an array and compute a new array.
const listCopy = require('./100-data').list;
console.log(listCopy);
console.log(listCopy.map((x, y) => x * y));
