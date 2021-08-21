// Install and implement template engine PUG

const path = require('path');

const express = require('express');

const rootDir = require('../util/path');
const adminData = require('./9-admin');

const router = express.Router();

router.get('/', (req, res, next) => {
    console.log(adminData.products)
    res.render('shop')
});

module.exports = router;