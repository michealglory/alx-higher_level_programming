#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let count = 0; count < x; count++) {
    let i = 0;
    let value = '';

    while (i < x) {
      value = value + 'X';
      i++;
    }
    console.log(value);
  }
}
