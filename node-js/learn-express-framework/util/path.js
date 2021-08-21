const path = require('path')

// process.mainModule.filename is responsible to give path of 
// file which is required to run app e.g. app.js
module.exports = path.dirname(process.mainModule.filename)