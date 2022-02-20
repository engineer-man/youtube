// node.js style callbacks
function1(args, (err, data) => {
    function2(args, (err, data) => {
        function3(args, (err, data) => {

        });
    });
});

// promise style callbacks
function1(args)
    .then(data => {
        return function2(args);
    })
    .then(data => {
        return function3(args);
    })
    .catch(err => {
        console.log(err);
    });

// async/await style
try {
    let data1 = await function1(args);
    let data2 = await function2(args);
    let data3 = await function3(args);

    function4().then(data => {
        console.log('done');
    });
} catch (e) {
    console.log(e);
}
