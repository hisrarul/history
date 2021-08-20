// Using express router
const path = require('path')
const express = require('express')
const bodyParser = require('body-parser')

const app = express();

const adminRoutes = require('./routes/6-admin');
const shopRoutes = require('./routes/6-shop');

app.use(bodyParser.urlencoded({extended: false}));

app.use(adminRoutes);
app.use(shopRoutes);

app.use((req, res, next) => {
    res.status(404).sendFile(path.join(__dirname, 'views', 'error.html'))
});

app.listen(3000);