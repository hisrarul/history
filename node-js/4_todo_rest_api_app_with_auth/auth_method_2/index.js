const express = require('express');
const bodyParser = require("body-parser");
const pool = require("./db");
const path = require('path');
const sha512 = require('crypto-js/sha512');

const app = express();

app.use(bodyParser.urlencoded({extended: false}))

// Routes

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
    const sql = "select username from auth_method2 where username = $1 and password = $2"
    const result = await pool.query(sql, [req.body.uname, sha512(req.body.psw)]);

    //fail
    if (result.rowCount === 0)
        res.send({"error": "Incorrect username or password"})
    else
        res.send({"success": "Logged in successfully!"})
})

// Register user
app.post("/register", async (req, res) => {
    //check if user exist 
    const sql = "select username from auth_method2 where username = $1"
    const result = await pool.query(sql,
                             [req.body.uname]);
    //success, user is not there create it
    if (result.rowCount === 0)
    {
        await pool.query("insert into auth_method2 (username, password) values ($1,$2)",
        [req.body.uname,sha512(req.body.psw)]);
        res.send({"success": "User created successfully"})

    } 
    else
        res.send({"error": "User already exists.."})
});

// get all todos
app.get("/todos", async(req, res) => {
    try {
        const allTodos = await pool.query("SELECT * from todo")
        res.json(allTodos.rows)
    } catch (err) {
        console.error(err.message)
    }
})

// get a todo
app.get("/todos/:id", async(req, res) => {
    const { id } = req.params
    try {
        const aTodo = await pool.query("SELECT description FROM todo WHERE todo_id = $1", [id]);
        res.json(aTodo.rows)
    } catch (err) {
        console.error(err.message)
    }
})

// Create a todo
app.post("/todos", async(req, res) => {
    try {
        const { description } = req.body;
        const newTodo = await pool.query("INSERT INTO todo (description) VALUES ($1) RETURNING *", [description]);
        res.json(newTodo.rows[0]);
    } catch (err) {
        console.error(err.message) 
    }
})

// update a todo
app.put("/todos/:id", async(req, res) => {
    try {
        const { id } = req.params
        const { description } = req.body
        const updateTodo = await pool.query("UPDATE todo SET description = $1 WHERE todo_id = $2", [description, id])
        res.json("Todo has updated!")
    } catch (err) {
        console.log(err.message)
    }
})

// delete a todo
app.delete("/todos/:id", async(req, res) => {
    try {
        const { id } = req.params
        const deleteTodo =  await pool.query("DELETE FROM todo WHERE todo_id = $1", [id])
        res.json("Todo was successfully deleted!")
    } catch (err) {
        console.log(err)
    }
})

app.listen(5000, () => {
    console.log("server is listening on port 5000")
})