//Team Blue Duck: Sean Ging, Patrick Ging
//Softdev, period 1
//K31
//2022-02-16



//DOM stuff
var c = document.getElementById("slate");
var stopButton = document.getElementById("stopButton");
var startButton = document.getElementById("startButton");
var dvdImage = document.getElementById("dvdImage");
var ctx = c.getContext("2d");


// Other stuff for dvd and movement
var dvdHeight = dvdImage.height;
var dvdWidth = dvdImage.width;

var totalVelocity = 5;


// why this?
// to give it an arbitrary direction
var arbitraryAngle = Math.random();

var xVelocity = totalVelocity * Math.cos(arbitraryAngle * 2 * Math.PI); 
var yVelocity = totalVelocity * Math.sin(arbitraryAngle * 2 * Math.PI);

//


// ^^^^^^ assuming that they're equal, it's too much 
// of a pain to use cos and sin with changing x and y velocity 
// I also don't think that's how the DVD bouncer operates.


//x and y position VVVVVV
var x = c.width / 2  - dvdWidth;
var y = c.height / 2 - dvdHeight;

var rID= null;
// placeholders for now....




function clear(e) {
  ctx.clearRect(0,0,c.width, c.height);
}


function startDvd(e) {
  clear(e);
  ctx.beginPath();
  ctx.drawImage(dvdImage, x, y, dvdWidth, dvdHeight);
  ctx.fill();
  ctx.stroke();

	if (y < 0 || y > c.height - dvdHeight) {
	
	/*
		why y > c.height - dvdHeight?
		
		because of the fact tha things are not place at center and
		are compared to the disctance of the top left most corner, we
		do - dvdHeight or - dvdWidth to reaccount for it, so it changes direction
		when the lower right corner collides instead....
	*/
	
	
	// if there's a collision, make the 
	// dvd move in the opposite y Direction
		yVelocity = yVelocity * -1;
	}
	if (x < 0 || x > c.width - dvdWidth) {
	// if there's a collision, make the 
	// dvd move in the opposite x Direction
		xVelocity = xVelocity * -1;
	}

	x += xVelocity;
	y += yVelocity;

	//remember to change the callback lmao V_V
  rID =  window.requestAnimationFrame(startDvd);

  }
var stop = () => {
  window.cancelAnimationFrame(rID);
}


document.getElementById("startButton").addEventListener("click", startDvd);
document.getElementById("stopButton").addEventListener("click",  stop);











