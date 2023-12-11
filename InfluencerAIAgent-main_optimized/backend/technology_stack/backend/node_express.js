const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const cors = require('cors');

// Import models
const { UserProfile, BrandCollaboration, ContentIdea } = require('./database/mongodb');

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Define routes
app.get('/api/influencers', async (req, res) => {
  try {
    const profiles = await UserProfile.find();
    res.json(profiles);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get('/api/influencers/collaborations', async (req, res) => {
  try {
    const collaborations = await BrandCollaboration.find();
    res.json(collaborations);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get('/api/content-ideas', async (req, res) => {
  try {
    const ideas = await ContentIdea.find();
    res.json(ideas);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ... define other routes

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});