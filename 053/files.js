const fs = require('fs');


let read_options = {
    encoding: 'utf-8',
    flag: 'r'
};

// read
fs.readFile('file.txt', read_options, (err, data) => {
    console.log(data.toString());
});


let write_options = {
    encoding: 'utf-8',
    flag: 'w',
    mode: 0o666
};

// write
fs.writeFile('file.txt', 'hello', write_options, err => {
    if (err) {
        // do something with error
    }
});


// delete
fs.unlink('file.txt', err => {
    if (err) {
        // do something with error
    }
});
