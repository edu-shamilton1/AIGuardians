// ./src/index.js

// importing the dependencies
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const path = require('path');

var telementyData = [];


// defining the Express app
const app = express();

app.use('/', express.static(path.join(__dirname, 'public')));

var userRoutes = require('./routes/user')(telementyData);
var llmRoutes = require('./routes/llm')(telementyData);

// defining an array to work as the database (temporary solution)
const ads = [
  {title: 'Hello, world (again)!'}
];

// adding Helmet to enhance your API's security
app.use(helmet());

// using bodyParser to parse JSON bodies into JS objects
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// enabling CORS for all requests
app.use(cors());

// adding morgan to log HTTP requests
app.use(morgan('combined'));

// set routes
app.use('/user', userRoutes);
app.use('/llm', llmRoutes);

app.get('/getTelementryData', (req, res) => {
  res.json(telementyData);
});

// defining an endpoint to return all ads
app.get('/status', (req, res) => {
  res.send(ads);
});

// starting the server
app.listen(3001, () => {
  console.log('listening on port 3001');
});
