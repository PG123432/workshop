/*
Patrick Ging, Sean Ging
Period 1
K27
February 6, 2022
*/

function fib(num){
	// standard fibonacci function
	// slower version
	if (num < 2) {return num;}

	return fib(num-1) + fib(num-2);
}

function factorial(num){
	// standard factorial func
	// likely the slower version (I forgot the faster one)
	if (num == 0) {return 1;}

	return num * factorial(num-1);
}