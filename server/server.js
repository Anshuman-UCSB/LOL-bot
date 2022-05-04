const express = require("express");
require("dotenv").config();
const app = express();

const DEBUG = true;
const LEADER = 1;
const MAXID = DEBUG ? 2 : 5;

var Client = {
  id: null,
  instr: "wait",
};

var config = {
  clients: [],
  id: 1,
  lobbyID: "",
};

app.get("/register", (req, res) => {
    if (config.id != MAXID) {
        res.json({"id": config.id})
    }
});

app.get("/instr/:id", (req, res) => {});

app.get("lobby", (req, res) => {
  res.json(config.lobbyID);
});

app.post("/tasks/:id", (req, res) => {});

app.post("/lobby", (req, res) => {});

app.listen(process.env.PORT, () => {
  console.log(`Listening on port: ${process.env.PORT}`);
});
