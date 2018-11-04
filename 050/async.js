function a() {
    return Promise.resolve('a')
}
async function b() {
    return Promise.resolve('b')
}
async function c() {
    return 'c'
}
console.log(a())
console.log(b())
console.log(c())
