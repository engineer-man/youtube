const cp = require('child_process');
const num1 = 5;
const num2 = 11;

cp.exec('python3 py.py ' + num1 + ' ' + num2, (error, out, err) => {
    console.log(out);
});
