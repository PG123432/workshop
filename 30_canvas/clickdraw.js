

// clickdraw.js



var c = document.getElementById('slate');

var ctx = c.getContext("2d"); //2D
//global state var
var mode = "rect";

// e means event
var toggleMode = (e) => {
  console.log("toggleing..............");
  if(mode === "rect"){
    mode= "arc";
  }
  else{
    mode= "rect";
  }
}


function drawRect = (e) =>{
  console.log("draw rect");
  mouseX= e.offsetX; //position of mouse
  mouseY= e.offsetY; //position
  ctx.fillRect(mouseX, mouseY, 50, 100);
  console.log("mouseclick at ", mouseX, mouseY);
}

function drawCircle = (e) => {
  console.log("drawCircle");
  mouseX= e.offsetX;
  mouseY= e.offsetY;
  ctx.beginPath(); //resets each time
  ctx.arc(mouseX, mouseY, 50, 0, Math.PI);
  ctx.fill();
  console.log("mouseclick at ", mouseX, mouseY);
}


function draw = (e) =>{
  console.log("drawing");
  if(mode=== "rect"){
    drawRect(e);
  }
  else{
    drawCircle(e);
  }
}


function wipeCanvas = (e) =>{
  ctx.clearRect(0,0, c.width, c.heigth); //makes all of canvas blank
}

c.addEventListener("click", draw);


var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click, wipeCanvas);

var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
