#!/usr/bin/node
const argmt = parseInt(process.argv[2]);
let i = 0;
if (isNaN(argmt))
	console.log('Missing size');
else {
	while (i < argmt) {
		console.log('x'.repeat(argmt));
		i++;
	}
}
