const express = require('express');
require('dotenv').config()
const app = express();

const DEBUG = true;

var config = {
    clients: [],
    id: 0,
    lobbyID: ""
}

app.get("/register", (req, res) => {

})

app.get("/instr/:id", (req, res) => {

})

app.get("lobby", (req, res) => {
    res.json(config.lobbyID)
})

app.post("/tasks/:id", (req, res) => {

})

app.post("/lobby", (req, res) => {

})



app.listen(process.env.PORT, () => {
    console.log(`Listening on port: ${process.env.PORT}`);
})