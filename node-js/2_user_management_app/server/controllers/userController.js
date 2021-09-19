const mysql = require('mysql')

const pool = mysql.createPool({
    connectionLimit: 100,
    host           : process.env.DB_HOST,
    user           : process.env.DB_USER,
    password       : process.env.DB_PASS,
    database       : process.env.DB_NAME
});


exports.view = (req, res) => {
    pool.getConnection((err, connection) => {
        if(err) throw err;
        console.log('Connected as ID ' + connection.threadId);
        // Use the connection
        connection.query('SELECT * FROM users where status="active"', (err, rows) => {
            // When done with connection, release it
            connection.release();
            if (!err) {
                res.render('home', { rows });
            } else {
                console.log(err);
            }
            console.log('The data from user table: \n', rows);
        });
    });  
}

exports.find = (req, res) => {
    pool.getConnection((err, connection) => {
        if(err) throw err;
        console.log('Connected as ID ' + connection.threadId);
        let searchTerm = req.body.search;
        // Use the connection
        connection.query('SELECT * FROM users WHERE status="active" AND (first_name LIKE ? OR last_name LIKE ?)', ['%' + searchTerm + '%', '%' + searchTerm + '%'], (err, rows) => {
            // When done with connection, release it
            connection.release();
            if (!err) {
                res.render('home', { rows });
            } else {
                console.log(err);
            }
            console.log('The data from user table: \n', rows);
        });
    });
}

exports.form = (req, res) => {
    res.render('add-user')
};

exports.create = (req, res) => {
    const { first_name, last_name, email, phone, comments } = req.body
    pool.getConnection((err, connection) => {
        if(err) throw err;
        console.log('Connected as ID ' + connection.threadId);
        let searchTerm = req.body.search;
        // Use the connection
        connection.query('INSERT INTO users SET first_name = ?, last_name = ?, email = ?, phone = ?, comments = ?', [first_name, last_name, email, phone, comments], (err, rows) => {
            // When done with connection, release it
            connection.release();
            if (!err) {
                res.render('add-user', {alert: 'User added successfully.'});
            } else {
                console.log(err);
            }
            console.log('The data from user table: \n', rows);
        });
    });
}

// Edit user
exports.edit = (req, res) => {
    pool.getConnection((err, connection) => {
        if(err) throw err;
        console.log('Connected as ID ' + connection.threadId);
        // Use the connection
        connection.query('SELECT * FROM users where id = ?', [req.params.id], (err, rows) => {
            // When done with connection, release it
            connection.release();
            if (!err) {
                res.render('edit-user', { rows });
            } else {
                console.log(err);
            }
            console.log('The data from user table: \n', rows);
        });
    });
}

// Update user
exports.update = (req, res) => {
    const { first_name, last_name, email, phone, comments } = req.body
    pool.getConnection((err, connection) => {
        if(err) throw err;
        console.log('Connected as ID ' + connection.threadId);
        connection.query('UPDATE users SET first_name = ?, last_name = ?, email = ?, phone = ?, comments = ? where id = ?', [first_name, last_name, email, phone, comments, req.params.id], (err, rows) => {
            connection.release();
            if (!err) {
                // This have copied to avoid the empty form loop
                pool.getConnection((err, connection) => {
                    if(err) throw err;
                    console.log('Connected as ID ' + connection.threadId);
                    connection.query('SELECT * FROM users where id = ?', [req.params.id], (err, rows) => {
                        connection.release();
                        if (!err) {
                            res.render('edit-user', { rows, alert: `${first_name} has been updated successfully!` });
                        } else {
                            console.log(err);
                        }
                        console.log('The data from user table: \n', rows);
                    });
                });
            } else {
                console.log(err);
            }
            console.log('The data from user table: \n', rows);
        });
    });  
}