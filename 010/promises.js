const q = require('q');

// callback hell
step1((err, value1) => {
    if (err) {
        // handle error for step1
    }
    step2(value1, (err, value2) => {
        if (err) {
            // handle error for step2
        }
        step3(value2, (err, value3) => {
            if (err) {
                // handle error for step3
            }
            step4(value3, (err, value4) => {
                if (err) {
                    // handle error for step4
                }
                step5(value4, (err, value5) => {
                    if (err) {
                        // handle error for step5
                    }
                    step6(value5, (err, value6) => {
                        if (err) {
                            // handle error for step6
                        }
                        // finally, do something with value6
                        console.log(value6);
                    });
                });
            });
        });
    });
});








// promise style
return step1()
    .then(value1 => {
        return step2(value1)
    })
    .then(value2 => {
        return step3(value2)
    })
    .then(value3 => {
        return step4(value3)
    })
    .then(value4 => {
        return step5(value4)
    })
    .then(value5 => {
        return step6(value5)
    })
    .then(value6 => {
        // finally, do something with value6
        console.log(value6);
    })
    .catch(err => {
        // handle error for everything regardless of where it came from
    });












// .then() example
return something_async_single_result()
    .then(result => {
        // do something with result
    });















// .spread() example
return something_async_three_results()
    .spread((result1, result2, result3) => {
        // do something with each result
    });
