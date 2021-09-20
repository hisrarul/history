const express = require('express');
const bodyParser = require("body-parser");
const pool = require("./db");
const path = require('path');
const sha512 = require('crypto-js/sha512');
const crypto = require('crypto')
const bcrypt = require('bcrypt')

const app = express();

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

// login page
app.get("/login", (req, res) => {
    try {
        res.sendFile(path.join(__dirname, 'login.html'))
    } catch (err) {
        console.log(err)
    }
});

// User login
app.post("/login", async (req, res) => {
    try {
        const sql = "select * from auth_method5 where username = $1"
        const result = await pool.query(sql, [req.body.uname]);

        // fail
        if (result.rowCount === 0)
            res.send({ "error": "User doesn't exist" })
        else {
            //get the encrypted data
            const encryptedData = result.rows[0].userdata;

            //attempt to decrypt using the user password
            const data = decryptAES(encryptedData, req.body.psw);

            //send the data to the user
            res.send({"data": data});
        }
    } catch (err) {
        console.log(err)
    }
})

// Register user
app.post("/register", async (req, res) => {
    //check if user exist 
    const sql = "select username from auth_method5 where username = $1"
    const result = await pool.query(sql, [req.body.uname]);

    //success, user is not there create it
    if (result.rowCount === 0) {
        const data = encryptAES(req.body.uname, req.body.psw)
        await pool.query("insert into auth_method5 (username, userdata) values ($1,$2)", [req.body.uname, data]);
        res.send({ "success": "User created successfully" })
    }
    else
        res.send({ "error": "User already exists.." })
});

// get all todos
app.get("/todos", async (req, res) => {
    try {
        const allTodos = await pool.query("SELECT * from todo")
        res.json(allTodos.rows)
    } catch (err) {
        console.error(err.message)
    }
})

// get a todo
app.get("/todos/:id", async (req, res) => {
    const { id } = req.params
    try {
        const aTodo = await pool.query("SELECT description FROM todo WHERE todo_id = $1", [id]);
        res.json(aTodo.rows)
    } catch (err) {
        console.error(err.message)
    }
})

// Create a todo
app.post("/todos", async (req, res) => {
    try {
        const { description } = req.body;
        const newTodo = await pool.query("INSERT INTO todo (description) VALUES ($1) RETURNING *", [description]);
        res.json(newTodo.rows[0]);
    } catch (err) {
        console.error(err.message)
    }
})

// update a todo
app.put("/todos/:id", async (req, res) => {
    try {
        const { id } = req.params
        const { description } = req.body
        console.log(description)
        const updateTodo = await pool.query("UPDATE todo SET description = $1 WHERE todo_id = $2", [description, id])
        res.json("Todo has updated!")
    } catch (err) {
        console.log(err.message)
    }
})

// delete a todo
app.delete("/todos/:id", async (req, res) => {
    try {
        const { id } = req.params
        const deleteTodo = await pool.query("DELETE FROM todo WHERE todo_id = $1", [id])
        res.json("Todo was successfully deleted!")
    } catch (err) {
        console.log(err)
    }
})

app.listen(5000, () => {
    console.log("server is listening on port 5000")
})

function encryptAES(plainText, key) {

    const encrypt = crypto.createCipher('aes256', key);
    let encrypted = encrypt.update(plainText, 'utf8', 'hex');
    encrypted += encrypt.final('hex')
    return encrypted;
}

function decryptAES(encryptedText, key) {
    try {
        const decrypt = crypto.createDecipher('aes256', key);
        let decrypted = decrypt.update(encryptedText, 'hex', 'utf8')
        decrypted += decrypt.final()
        return decrypted
    }
    catch (err) {
        return err;
    }
}