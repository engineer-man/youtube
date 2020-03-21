// node style callback
some_async_fn((err, data) => {

});

some_async_fn()
    .then(result => {
        // do something with result
    });

let result = await some_async_fn();
// do something with result
