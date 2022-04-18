#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.size));
      } else {
        console.log('C'.repeat(this.size));
      }
    }
  }
};
