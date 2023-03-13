#!/usr/bin/node
const argmt = parseInt(process.argv[2]);
if (isNaN(argmt))
	console.log('Not a number');
else
	console.log('My number: ' + argmt);
