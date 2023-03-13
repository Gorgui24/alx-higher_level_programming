#!/usr/bin/node
const argmt = parseInt(process.argv[2]);
function factorial(n) {
	if (isNaN(n) || n === 0)
		console.log('1');
	else
		console.log(n * factorial(n - 1));
}
factorial(argmt);
