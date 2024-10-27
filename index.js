const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const { Server } = require('socket.io');
dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

mongoose.connect(process.env.DB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Database connected'))
  .catch((error) => console.error('Database connection error:', error));

app.use(express.json());

// Socket.IO for real-time updates
const httpServer = app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
const io = new Server(httpServer);

io.on('connection', (socket) => {
  console.log('New client connected');
  // Handle real-time updates here
});

// Example of protected route
app.get('/protected', authenticateJWT, (req, res) => {
  res.send('Secure route accessed');
});

function authenticateJWT(req, res, next) {
  const token = req.header('Authorization');
  if (!token) return res.status(401).send('Access denied');

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.status(403).send('Invalid token');
    req.user = user;
    next();
  });
}
