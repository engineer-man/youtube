// this function returns another function
let outer = () => {
    let num = 4;

    // this function that is returned
    // encloses the outer scope
    return () => {
        // this will output 4 because it enclosed num
        // when it was created
        console.log(num);
    };
};

let inner = outer();
inner();
