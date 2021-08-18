// Node module

const http = require('http');


const routes = require('./6-node-module-routes')

// Different ways to import a node module

// const server = http.createServer(routes);
// const server = http.createServer(routes.handler)

const server = http.createServer(routes.handler)
console.log(routes.someKey)

server.listen(3000);