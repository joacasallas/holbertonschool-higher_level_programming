#!/usr/bin/node
// prints the number of arguments already printed and the new argument value.
let number_argument = 0;
exports.logMe = function (item) {
  console.log(`${number_argument}: ${item}`);
  number_argument++;
};
