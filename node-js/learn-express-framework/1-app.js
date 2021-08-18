const express = require('express')

const app = express();

app.use('/', (req, res, next) => {
    console.log('In the middleware!')
    next()
})

app.use((req, res, next) => {
    console.log('In another middleware!')
    res.send('<h1>Hello from Kamran!</h1><h2>Hello from Luck!</h2>')
})

app.listen(3000)