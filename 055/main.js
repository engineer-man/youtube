const fs = require('fs');
const library = require('./library.js');
const library2 = require('./library2.js');
const library3 = require('./library3.js');

console.log(library.name);
console.log(library.reverse(library.name));

console.log(library2.name);
console.log(library2.reverse(library2.name));

console.log(library3.name);
console.log(library3.reverse(library3.name));
