const express = require("express");
require("dotenv").config();
const services = require("./services")
const app = express();

const DEBUG = true;
const LEADER = 0;
const MAXID = DEBUG ? 2 : 5;

function Client(id) {
  this.id = id;
  this.instr = "wait";

  this.user;
  this.pass;
};

var config = {
  clients: [],
  id: 0,
  lobbyID: "",
};

app.get("/register", (req, res) => {
  if (config.id < MAXID) {
    config.clients.push(new Client(config.id));

    if (config.id == LEADER) {
        services.setup();
    }

    return res.json({ id: config.id++});
  }
  res.status(500).json({ "msg": "error" });
});

if (DEBUG) {
    app.get("/reset", (req, res) => {
        config.id = 0;
        res.json({"msg": "success"})
    })
}

app.get("/instr/:id", (req, res) => {
    res.json({"instr": config.clients[req.params.id].instr})
});

app.get("/lobby", (req, res) => {
  res.json({"id": config.lobbyID});
});

app.post("/tasks/:id", (req, res) => {

});

app.post("/lobby/:id", (req, res) => {
    config.lobbyID = req.params.id;
    res.json({"msg" : "success"})
});

app.listen(process.env.PORT, () => {
  console.log(`Listening on port: ${process.env.PORT}`);
});
