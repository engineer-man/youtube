#!/usr/bin/env node

const start_num = process.argv[2];
const count = process.argv[3];

let list = [];

for (i = 0; i < count; ++i) {
    list.push(i * start_num);
}

let sum = 0;
let divisible = 0;

list.forEach(num => {
    sum += num;
    if (num % 10 == 0) ++divisible;
});

console.log(sum, divisible);
