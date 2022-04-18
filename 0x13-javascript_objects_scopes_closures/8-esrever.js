#!/usr/bin/node
// Write a function that returns the reversed version of a list
exports.esrever = function (list) {
  const listCopy = [];
  for (let i = 0; list[i] != null; i++) {
    listCopy.unshift(list[i]);
  }
  return listCopy;
};
