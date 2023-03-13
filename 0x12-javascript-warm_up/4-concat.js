#!/usr/bin/node
const argmt = process.argv[2];
const argmt1 = process.argv[3];
if (argmt == null && argmt1 == null)
	console.log('undefined is undefined');
else if (argmt1 == null)
	console.log(argmt + ' is undefined');
else
	console.log(argmt + ' is ' + argmt1);
