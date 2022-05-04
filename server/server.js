const express = require('express');
require('dotenv').config()

const app = express();

app.get("/register", (req, res) => {

})

app.get("/instr/:id", (req, res) => {

})

app.post("/tasks/:id", (req, res) => {

})

app.post("/lobby", (req, res) => {

})


app.listen(process.env.PORT, () => {
    console.log(`Listening on port: ${process.env.PORT}`);
})