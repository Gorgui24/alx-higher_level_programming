#!/usr/bin/node
const argmt = parseInt(process.argv[2]);
let i = 0;
if (isNaN(argmt))
	console.log('Missing number of occurrences');
else {
	while (i < argmt) {
		console.log('C is fun');
		i++;
	}
}
