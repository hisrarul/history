const express = require('express')
const pool = require("./db");

const app = express();

app.use(express.json())     // Gives req.body

// Routes

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