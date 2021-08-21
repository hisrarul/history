// Sharing Data Across requests and users using variable

const path = require('path');

const express = require('express');

const rootDir = require('../util/path');
const adminData = require('./8-admin');

const router = express.Router();

router.get('/', (req, res, next) => {
    console.log(adminData.products)
    res.sendFile(path.join(rootDir, 'views', '8-shop.html'))
});

module.exports = router;