const express = require('express')

const app = express();

app.use('/', (req, res, next) => {
    console.log('This always runs!')
    next();
});

app.use('/products', (req, res, next) => {
    console.log('In the middleware')
    res.send('<html><body><ul><li>Shampoo</ul></li></body></html>')
});

app.use('/', (req, res, next) => {
    console.log('In another middleware!')
    res.send('<h1>Hello from Kamran!</h1><h2>Hello from Lucky!</h2>')
});

app.listen(3000)