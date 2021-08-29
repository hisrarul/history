// Install and implement template engine PUG

const path = require('path');

const express = require('express');

const rootDir = require('../util/path');
const adminData = require('./12-admin');

const router = express.Router();

router.get('/', (req, res, next) => {
    const products = adminData.products
    for (let i of products) {
        console.log(i.title)
    }
    res.render('12-shop', {prods: products, pageTitle: 'My Dynamic Shop', path: '/'});
});

module.exports = router;