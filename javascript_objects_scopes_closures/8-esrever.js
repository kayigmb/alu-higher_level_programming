#!/usr/bin/Node
exports.esrever = function (list) {
  const input = [];
  for (let i = list.length - 1; i >= 0; i--) {
    input.push(list[i]);
  }
  return input;
};
