#!/usr/bin/env node
var fs = require('fs');
var outfile = "hello.txt";

var output = [];

var isPrimeNumber = function( number ) {
    if (number == 1 || number == 2) {
        return true;
    }
    for (var j=2;j<number;j++) {
        if (number % j == 0) {
            return false;
        }
    }
    return true;
}
var i = 2;
while(output.length != 100) {
    if (isPrimeNumber(i)) {
        output.push(i);
    }
    i +=1;
}
console.log(output.length);
var out = output.join(",");

fs.writeFileSync(outfile, out);
console.log("Script: " + __filename + "\nWrote: " + out + "\nTo: " + outfile);