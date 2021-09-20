const Pool = require('pg').Pool;

const pool = new Pool({
    user: "postgres",
    password: "password",
    database: "auth",
    host: "localhost",
    port: 5432
});

const todoPool = new Pool({
    user: "postgres",
    password: "password",
    database: "auth",
    host: "localhost",
    port: 5432
})


module.exports = pool;
module.exports = todoPool;