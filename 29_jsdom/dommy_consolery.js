/*
Patrick and Sean Ging Period 1
FEB 8, 2022
K28
*/
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};



function gcd(a,b){

  var min = Math.min(a,b);
  var max = Math.max(a,b);

  if (max%min ==0) {

      document.getElementById("h").innerHTML = b;
      return b;
  };
  return gcd(max, max%min);
}


function fibHelper(num){
  // standard fibonacci function
  // slower version
  if (num < 2) {
    return num;}

  return fib(num-1) + fib(num-2);
}


function fib(num){
    var x = fibHelper(num);
    document.getElementById("div1").innerHTML = x;
}




function factorialHelper(num){
  // standard factorial func
  // likely the slower version (I forgot the faster one)
  if (num == 0) {return 1;}

  return num * factorial(num-1);
}


function factorial(num) {
  var y = factorialHelper(num);
  document.getElementById("div2").innerHTML = y;
  return y; 
}



document.getElementById("button_fac").addEventListener("click", function() {factorial(3);});
document.getElementById("button_fib").addEventListener("click", function() {fib(3);});
document.getElementById("button_gcd").addEventListener("click", function() {gcd(18, 12);});
//insert your implementations here for...
// FIB
// FAC
// GCD