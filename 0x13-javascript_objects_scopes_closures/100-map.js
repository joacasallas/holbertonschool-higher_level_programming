#!/usr/bin/node
// import an array and compute a new array.
const list = require('./100-data').list;
console.log(list);
console.log(list.map((x, y) => x * y));
