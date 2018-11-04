const floppy = require('floppy');

var run = async () => {
    const data1 = await floppy.load('disk1');

    await floppy.prompt('please insert disk 2');
    const data2 = await floppy.load('disk2');

    await floppy.prompt('please insert disk 3');
    const data3 = await floppy.load('disk3');

    await floppy.prompt('please insert disk 4');
    const data4 = await floppy.load('disk4');

    await floppy.prompt('please insert disk 5');
    const data5 = await floppy.load('disk5');

    await floppy.prompt('please insert disk 6');
    const data6 = await floppy.load('disk6');

    // if node.js would have existed in 1995
};

run();
