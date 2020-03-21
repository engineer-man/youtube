// override or extend built in functionality
String.prototype.lolcase = function() {
    let value = this.valueOf();
    let final = '';

    for (let i = 0; i < value.length; ++i) {
        final += i % 2 === 0
            ? value[i].toUpperCase()
            : value[i].toLowerCase()
    }

    return final;
};

console.log('brian'.lolcase());

return;

// old way of oop
let base = function(init_var) {
    // constructor stuff here

    // public class properties
    this.num1 = 1;
    this.num2 = 2;
    this.num3 = 3;

    // private class properties
    let num1 = 1;
    let num2 = 2;
    let num3 = 3;

    // class methods
    this.sum = () => this.num1 + this.num2 + this.num3;
};

let child = function(init_var) {
    // constructor stuff here
    this.num3 = init_var;
};

// extends
child.prototype = new base();

// instantiate child which inherits base
let obj = new child(4);

console.log(obj.num1, obj.num2, obj.num3, obj.sum());
