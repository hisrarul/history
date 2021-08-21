// Install and implement template engine PUG

const path = require('path');

const express = require('express');

const rootDir = require('../util/path');
const adminData = require('./10-admin');

const router = express.Router();

router.get('/', (req, res, next) => {
    const products = adminData.products
    res.render('10-shop', {prods: products, pageTitle: 'My Dynamic Shop', path: '/'});
});

module.exports = router;