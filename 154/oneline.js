// normal
switch (a) {
    case 1:
        console.log('one');
        break;
    case 2:
        console.log('two');
        break;
    default:
        console.log('none');
}

// one liner
console.log(a === 1 ? 'one' : a === 2 ? 'two' : 'none');
