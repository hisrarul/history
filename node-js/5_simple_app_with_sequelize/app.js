const express = require('express');
const exphbs = require('express-handlebars');
const bodyParser = require('body-parser');
const path = require('path');
const db = require('./config/database')

// Test the connection
db.authenticate()
  .then(() => console.log('Database connected..'))
  .catch(err => console.log('Error' + err))

const app = express();

// Handlebars
app.engine('handlebars', exphbs({ defaultLayout: 'main'}));
app.set('view engine', 'handlebars');

// Body parser
app.use(bodyParser.urlencoded({ extended: false }));

// Set static folder
app.use(express.static(path.join(__dirname, 'public')))

// Gig routes
app.use('/gigs', require('./routes/gigs'));

// Index route
app.use('/', (req, res) => {
  res.render('index', { layout: 'landing'})
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, console.log(`Server started on port ${PORT}`));