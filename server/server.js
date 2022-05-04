const express = require('express');
require('dotenv').config()

const app = express();

app.get("/register", (req, res) => {

})

app.get()


app.listen(process.env.PORT, () => {
    console.log(`Listening on port: ${process.env.PORT}`);
})