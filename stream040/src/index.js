(ctx => {
    return ctx.keys().map(ctx);
})(require.context('./js', true, /\.js$/));

(ctx => {
    return ctx.keys().map(ctx);
})(require.context('./jsx', true, /\.jsx$/));

(ctx => {
    return ctx.keys().map(ctx);
})(require.context('./less', true, /\.less$/));
