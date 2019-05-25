const ffi = require('ffi');

const c_lib = ffi.Library('./c/main.so', {
    hello: ['void', []],
    sum: ['int', ['int', 'int']]
});
const cpp_lib = ffi.Library('./cpp/main.so', {
    hello: ['void', []],
    sum: ['int', ['int', 'int']]
});
const go_lib = ffi.Library('./go/main.so', {
    Hello: ['void', []],
    Sum: ['int', ['int', 'int']]
});

console.log('\n\njavascript tests')

// c
c_lib.hello()
console.log(c_lib.sum(1, 2))

// cpp
cpp_lib.hello()
console.log(cpp_lib.sum(1, 2))

// go
go_lib.Hello()
console.log(go_lib.Sum(1, 2))
