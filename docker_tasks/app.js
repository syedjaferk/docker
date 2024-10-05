// app.js
const express = require('express');
const app = express();
 
// A simple route to return the status of the application
app.get('/health', (req, res) => {
    res.status(200).send('OK');
});
 
// Example main route
app.get('/', (req, res) => {
    res.send('Hello, Docker!');
});
 
// Start the server on port 3000
const port = 3000;
app.listen(port, () => {
    console.log(`App is running on http://localhost:${port}`);
});