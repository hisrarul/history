// Using express router

const express = require('express');

const router = express.Router();

router.get('/', (req, res, next) => {
    res.send('<h1>Item has been successfully added to the Cart.</h1>')
});

module.exports = router;