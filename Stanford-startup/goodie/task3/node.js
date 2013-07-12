var fs = require('fs');

var output = fs.readFileSync("task3/index.html");
var buffer = new Buffer(output, "utf-8");

console.log(buffer.toString());

