var reverse = str => {
    return str.split('').reverse().join('');
};

var uppercase = str => {
    return str.toUpperCase();
};

module.exports = {

    /**
     * transform will reverse and uppercase a string
     */
    transform(name) {
        name = reverse(name);
        name = uppercase(name);

        return name;
    }

};
