#!/usr/bin/node
// prints the number of arguments already printed and the new argument value.
let numberArgument = 0;
exports.logMe = function (item) {
  console.log(`${numberArgument}: ${item}`);
  numberArgument++;
};
