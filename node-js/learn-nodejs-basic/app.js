const http = require('http');

function rqListener(req, res) {
    // console.log(req)
    console.log(req.url, req.method, req.headers)
    // process.exit(); To quit event loop in node.js
}

const server = http.createServer(rqListener);

// http.createServer(function(req, res){
// });

// http.createServer((req, res) => {
//     console.log(req)
// });

server.listen(3000);


// Sending response
function rqListener(req, res) {
    console.log(req.url, req.method, req.headers)
    res.setHeader('Content-Type', 'text/html');
    res.write('<html>');
    res.write('<head><title>My First Page</title><head>');
    res.write('<body><h1>Hello from my Node.js server</h1></body>');
    res.write('</html>');
    res.end();
}