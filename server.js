const express = require('express');
const sqlite3 = require('sqlite3').verbose(); // Import sqlite3

const app = express();
const port = 3000;

// Create and connect to the SQLite database
const db = new sqlite3.Database('./data.db', sqlite3.OPEN_READWRITE, (err) => {
  if (err) {
    console.error(err.message);
  } else {
    console.log('Connected to the database');
  }
});

// Define routes for handling database queries
app.get('/getRandomWord', (req, res) => {
  db.get('SELECT yoruba, english FROM words ORDER BY RANDOM() LIMIT 1', (err, row) => {
    if (err) {
      console.error(err.message);
      res.status(500).send('Database error');
    } else {
      res.json(row); // Send the result as JSON
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
