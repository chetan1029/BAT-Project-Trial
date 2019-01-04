var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('autoprefixer');
var concat = require('gulp-concat');
var postcss = require('gulp-postcss');
var sourcemaps = require('gulp-sourcemaps');
var browserSync = require('browser-sync').create();
var reload = browserSync.reload;

// Run the Django development server
gulp.task('django', function() {
    const spawn = require('child_process').spawn;
    return spawn('python', ['manage.py', 'runserver'])
        .stderr.on('data', (data) => {
        console.log(`${data}`);
    });
});

// Compile main.sass into style.css
gulp.task('styles', function() {
    gulp.src('static/app/sass/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(concat('style.css'))
        .pipe(sourcemaps.init())
        .pipe(postcss([autoprefixer() ]))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('static/app/css/'));
});
gulp.task('sass', function(){
  gulp.src('static/app/sass/**/*.scss')
  .pipe(wait(700))
  .pipe(sass())
  .pipe(gulp.dest("static/app/css"))
  .pipe(cssnano({zindex: false}))
  .pipe(rename({ suffix: '.min' }))
  .pipe(gulp.dest("static/app/css"))
  .pipe(gulp.dest("static/dist/css"));
});

// Initiate browsersync and point it at localhost:8000
gulp.task('browsersync', function() {
    browserSync.init({
        notify: true,
        proxy: "localhost:8000",
    });
});

// Tell gulp to executed 'styles' when sass files change, and execute
// a browser reload when any file changes.
gulp.task('watch', function() {
    gulp.watch('./static/app/sass/**/*.scss', ['styles']);
    gulp.watch('./static/app/sass/**/*.scss', ['sass']);
    gulp.watch(['./**/*.{scss,css,html,py,js}'], reload);
});

// 'gulp' calls django, browsersync, and watch tasks
gulp.task('default', ['django', 'browsersync', 'watch']);
