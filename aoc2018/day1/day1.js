const fs = require('fs')

inputs = fs.readFileSync('inputs.txt')
    .toString()
    .trim()
    .split('\n')
    .map(i => +i);

// puzzle 1
console.log(inputs.reduce((a,b) => a+b, 0))

// puzzle 2
seen = new Set()
f = 0
for (;;) {
    inputs.forEach(input => {
        f += input
        if (seen.has(f)) {
            console.log(f)
            process.exit()
        }
        seen.add(f)
    });
}
