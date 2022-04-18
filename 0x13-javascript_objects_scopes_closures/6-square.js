#!/usr/bin/node
// Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
module.exports = class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  double () {
    super.double();
  }

  rotate () {
    super.rotate();
  }

  print () {
    super.print();
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
};
