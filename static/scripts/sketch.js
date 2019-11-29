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


var x = 50;
var y = 50;
var needRoute = false;
var ok_vertical = false;
var selected_route = 1;
var actual_y = 50;
var actual_x = 50;


function draw(){
  background(bg);
  // do i need to draw any route?
  if (needRoute){
    actual_x = x;
    actual_y = y;
    // get params for that route
    //selected_route = $('#selected_route').val();
    switch (selected_route){

      case 1:
        if (y < actual_y - 50){
          y++;
        }else{
          actual_y = y;
          ok_vertical = true;
        }
        if (ok_vertical && x <= actual_x + 550){
          x++;
        } else {
          selected_route = 2;
          //actual_x = x;
        }
        break;
      case 2:
        if (y <= 200){
          y++;
          actua
        }else {
          ok_vertical = true;
          //actual_y = y;
        }
        if (ok_vertical && x >=  180){  // eu sempre tenho q mover na vertical primeiro
          x--;
        } else {
          //actual_x = x;
        }
        break;
    //x_dest = all_routes[selected_route]['x']
    //y_dest = all_routes[selected_route]['y']
    }
  }
  fill(0);
  ellipse(x, y, 80, 80);
//i++;
}
