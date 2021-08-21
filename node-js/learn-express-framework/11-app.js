// Using Handlebars

const path = require('path')
const express = require('express')
const bodyParser = require('body-parser')
const expressHbs = require('express-handlebars')

const app = express();

app.engine('handlebars', expressHbs());
app.set('view engine', 'handlebars');
app.set('views', 'views');

const adminData = require('./routes/10-admin');
const shopRoutes = require('./routes/10-shop');

app.use(bodyParser.urlencoded({extended: false}));
app.use(express.static(path.join(__dirname, 'public')));

app.use(adminData.routes);
app.use(shopRoutes);

app.use((req, res, next) => {
    res.status(404).render('11-error', {pageTitle: 'Page Not Found!'})
});

app.listen(3000);