const cp = require('child_process');

const exec_options = {
    cwd: null,
    env: null,
    encoding: 'utf8',
    timeout: 0,
    maxBuffer: 200 * 1024,
    killSignal: 'SIGTERM'
};

// exec
cp.exec('ls -l', exec_options, (err, stdout, stderr) => {
    console.log('#1. exec')
    console.log(stdout);
});


// exec sync
try {
    const data = cp.execSync('ls -l', exec_options);
    console.log('#2. exec sync')
    console.log(data.toString());
} catch (err) {

}


const spawn_options = {
    cwd: null,
    env: null,
    detached: false
};

// spawn
const ls = cp.spawn('ls', ['-l'], spawn_options);

ls.stdout.on('data', stdout => {
    console.log('#3. spawn')
    console.log(stdout.toString());
});

ls.stderr.on('data', stderr => {
    console.log(stderr.toString());
});

ls.on('close', code => {
    // ended with code
});


// spawn sync
const { stdout, stderr, pid, status } = cp.spawnSync('ls', ['-l'], spawn_options);
console.log('#4. spawn sync')
console.log(stdout.toString());
