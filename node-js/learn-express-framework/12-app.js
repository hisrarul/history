// Using EJS

const path = require('path')
const express = require('express')
const bodyParser = require('body-parser')


const app = express();

app.set('view engine', 'ejs');
app.set('views', 'views');

const adminData = require('./routes/12-admin');
const shopRoutes = require('./routes/12-shop');

app.use(bodyParser.urlencoded({extended: false}));
app.use(express.static(path.join(__dirname, 'public')));

app.use(adminData.routes);
app.use(shopRoutes);

app.use((req, res, next) => {
    res.status(404).render('12-error', {pageTitle: 'Page Not Found!!'})
});

app.listen(3000);