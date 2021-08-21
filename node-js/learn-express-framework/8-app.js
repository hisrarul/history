// Sharing Data Across requests and users using variable

const path = require('path')
const express = require('express')
const bodyParser = require('body-parser')

const app = express();

const adminData = require('./routes/8-admin');
const shopRoutes = require('./routes/8-shop');

app.use(bodyParser.urlencoded({extended: false}));
app.use(express.static(path.join(__dirname, 'public')));

app.use(adminData.routes);
app.use(shopRoutes);

app.use((req, res, next) => {
    res.status(404).sendFile(path.join(__dirname, 'views', '8-error.html'))
});

app.listen(3000);