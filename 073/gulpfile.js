const gulp = require('gulp');
const babel = require('gulp-babel');
const concat = require('gulp-concat');
const react = require('gulp-react');
const watch = require('gulp-watch');
const plumber = require('gulp-plumber');
const cp = require('child_process');

gulp.task('react', () => {
    return gulp
        .src(['./components/**/*'])
        .pipe(plumber())
        .pipe(react())
        .pipe(babel({ presets: ['env'] }))
        .pipe(concat('all.js'))
        .pipe(gulp.dest('dist'))
});

gulp.task('default', () => {
    gulp.start(['react']);

    cp.exec('node_modules/.bin/http-server');

    watch(['./components/**/*'], () => gulp.start(['react']));
});
