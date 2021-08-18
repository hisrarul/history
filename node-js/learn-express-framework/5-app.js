// Using express router

const express = require('express')
const bodyParser = require('body-parser')

const app = express();

const adminRoutes = require('./routes/5-admin');
const shopRoutes = require('./routes/5-shop');

app.use(bodyParser.urlencoded({extended: false}));

app.use(adminRoutes);
app.use(shopRoutes);

app.use((req, res, next) => {
    res.status(404).send('<h1>Page Not Found!</h1>')
})

app.listen(3000);