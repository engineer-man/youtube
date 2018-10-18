// arrow functions
var nums = [1, 2, 3, 4];
nums.forEach(num => {
    console.log(num * 2);
});



// ===



// block scoping with let
for (let i = 0; i <= 4; ++i) {
    setTimeout(() => {
        console.log(i);
    }, 1000);
}



// ===



// default params
function test1(a, b, c = 3) {
    console.log('default params:', a + b + c);
}
test1(1, 2);



// ===



// variadic function arguments
function sum(...nums) {
    console.log(nums.reduce((acc, a) => a + acc, 0))
}

sum(1, 5, 7, 9, 9, 9, 18, 4, 6);



// ===



// spread operator
var a = [1, 2, 3];
var b = [...a, 4, 5];
console.log(b)



// ===



// property shorthand
var c = 'c';
var d = 'd';

var e = { c, d };



// ===



// computed object keys
var name = 'something';

var object = {
    [name]: 'cool'
};

console.log(object.something)



// ===



// method notation in objects
var methods = {
    foo() {
        console.log('foo');
    },
    bar() {
        console.log('bar');
    }
};



// ===



// array destructuring
var nums = [1, 2, 3];
var [ one, two, three ] = nums;

console.log(one, two, three);

// swap-a-roo
var [one, two] = [two, one];

console.log(one, two);



// ===



// object destructuring
var nums = { one: 1, two: 2, three: 3 };
var { one, two, three } = nums;

console.log(one, two, three);



// ===



// classes, getters
class thing {
    constructor(_id) {
        this._id = _id;
    }
    get id() {
        return this._id;
    }
}

var t = new thing(555);
console.log(t.id)



// ===



// generators
function* range(start, end) {
    while (start < end) {
        yield start;
        start += 1;
    }
}

for (let i of range(0, 10)) {
    console.log(i);
}
