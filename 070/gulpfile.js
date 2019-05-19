const gulp = require('gulp');
const babel = require('gulp-babel');
const react = require('gulp-react');
const watch = require('gulp-watch');
const plumber = require('gulp-plumber');
const cp = require('child_process');

gulp.task('react', () => {
    return gulp
        .src(['./component.jsx'])
        .pipe(plumber())
        .pipe(react())
        .pipe(babel({ presets: ['env'] }))
        .pipe(gulp.dest('.'))
});

gulp.task('default', () => {
    gulp.start(['react']);

    cp.exec('node_modules/.bin/http-server');

    watch(['./component.jsx'], () => gulp.start(['react']));
});
