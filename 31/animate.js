//Team Blue Duck: Sean Ging, Patrick Ging
//Softdev
//K31
//2022-02-16
//time spent: 1hr




var c = document.getElementById("slate");
var stopButton = document.getElementById("stopButton");
var startButton = document.getElementById("startButton");

var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

function clear(e) {
  ctx.clearRect(0,0,c.width, c.height);
}

var radius = 10;
var growing = true;
var rID= null;
var drawDot = (e) => {
  clear(e);

  //window.requestAnimationFrame(callback);
  // tells browser that you wish to perform animation
  ctx.beginPath();
  ctx.arc(c.width / 2, c.height / 2, radius, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();

  if (radius >= 300) {
    growing = false;
  }
  else if (radius == 1) {
  	growing = true;
  }
  
  
  
  if (growing){
    radius += 1.5;
  }
  else {
    radius -= 1.5;
  }

  rID =  window.requestAnimationFrame(drawDot);


  }
var stopIt = () => {
  window.cancelAnimationFrame(rID);
}


document.getElementById("startButton").addEventListener("click", drawDot);
document.getElementById("stopButton").addEventListener("click",  stopIt);










