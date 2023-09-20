i//LOGIN SERVER-SIDE JS
//

const express = require('express');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const mysql = require('mysql2'); // Import the MySQL library

const app = express();
const port = 3000;

// Create a MySQL database connection
const connection = mysql.createConnection({
    host: 'database-host', // replace placeholder
    user: 'username', // replace placeholder
    password: 'password', // replace placeholder
    database: 'database-name' // replace placeholder
});

// Connect to the database
connection.connect((error) => {
    if (error) {
        console.error('Database connection failed:', error);
    } else {
        console.log('Connected to the database');
    }
});

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Handle login POST request
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    
    // Query the database to find the user by username
    connection.query('SELECT * FROM users WHERE username = ?', [username], (dbError, results) => {
        if (dbError) {
            console.error('Database error:', dbError);
            return res.status(500).json({ success: false, message: 'Database error' });
        }

        // Check if a user with the given username exists
        if (results.length === 0) {
            return res.status(401).json({ success: false, message: 'Invalid username or password' });
        }

        const user = results[0];

        // Compare the provided password with the hashed password from the database
        bcrypt.compare(password, user.passwordHash, (bcryptError, result) => {
            if (bcryptError || !result) {
                // Passwords don't match
                return res.status(401).json({ success: false, message: 'Invalid username or password' });
            }

            // Successful login
            res.json({ success: true, message: 'Login successful' });
        });
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});



//REGISTRATION PAGE SERVER SIDE JS
//

const express = require('express');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const mysql = require('mysql2');

const app = express();
const port = 3000;

// Create a MySQL database connection
const connection = mysql.createConnection({
    host: 'localhost', //replace placeholder
    user: 'pharmacy_dev', //replace placeholder
    password: 'pharmacy_dev_pwd', //replace placeholder
    database: 'pharmacy_dev_db' //replace placeholder
});

// Connect to the database
connection.connect((error) => {
    if (error) {
        console.error('Database connection failed:', error);
    } else {
        console.log('Connected to the database');
    }
});

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Define Registration Route
app.post('/register', (req, res) => {
    const { username, email, password } = req.body;

    // Hash the password before storing it in the database
    bcrypt.hash(password, 10, (hashError, hash) => {
        if (hashError) {
            console.error('Password hashing error:', hashError);
            return res.status(500).json({ success: false, message: 'Registration failed' });
        }

        // Insert the user into the database
        connection.query('INSERT INTO users (username, email, passwordHash) VALUES (?, ?, ?)', [username, email, hash], (dbError, results) => {
            if (dbError) {
                console.error('Database error:', dbError);
                return res.status(500).json({ success: false, message: 'Registration failed' });
            }

            // Registration successful
            res.json({ success: true, message: 'Registration successful' });
        });
    });
});

// Start the Express Server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
