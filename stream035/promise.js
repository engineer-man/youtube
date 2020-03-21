(async () => {










let a = () => {
    return new Promise((resolve, reject) => {
        resolve(5);
    });
};

let num = await a();
console.log(num);

a().then(num => console.log(num));













})();
