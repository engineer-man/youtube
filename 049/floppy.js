const floppy = require('floppy');

return floppy.load('disk1')
    .then(data1 => {
        return floppy.prompt('please insert disk 2');
    })
    .then(() => {
        return floppy.load('disk2');
    })
    .then(data2 => {
        return floppy.prompt('please insert disk 3');
    })
    .then(() => {
        return floppy.load('disk3');
    })
    .then(data3 => {
        return floppy.prompt('please insert disk 4');
    })
    .then(() => {
        return floppy.load('disk4');
    })
    .then(data4 => {
        return floppy.prompt('please insert disk 5');
    })
    .then(() => {
        return floppy.load('disk5');
    })
    .then(data5 => {
        return floppy.prompt('please insert disk 6');
    })
    .then(() => {
        return floppy.load('disk6');
    })
    .then(data6 => {
        // if node.js would have existed in 1995
    });
