#!/usr/bin/node
let i = 0;
for (; i < process.argv.length; i++) {
  continue;
}
if (i < 3) {
  console.log('No argument');
} else if (i === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
