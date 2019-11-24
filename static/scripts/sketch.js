// sketch.js

var cnv;
let bg;

function centerCanvas() {
  var x = (windowWidth - width) / 2;
  var y = (windowHeight - height) / 2;
  cnv.position(x, y);
}

function setup() {
  bg = loadImage('/static/imgs/mapa.jpg' );
  cnv = createCanvas(901, 481);
  centerCanvas();
  //background(255, 0, 200);
}

function windowResized() {
  centerCanvas();
}

function draw(){
  background(bg);
  fill(0);
  ellipse(50, 50, 80, 80);
}
