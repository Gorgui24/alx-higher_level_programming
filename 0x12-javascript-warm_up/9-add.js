#!/usr/bin/node
const argmt = parseInt(process.argv[2]);
const argmt1 = parseInt(process.argv[3]);
function add(a, b) {
	if (isNaN(a) || isNaN(b))
		console.log('NaN');
	else
		console.log(a + b);
}
add(argmt, argmt1);
