const express = require('express');
const { route } = require('express/lib/application');
const router = express.Router()
const db = require('../config/database');
const Gig = require('../models/Gig')
const Sequelize = require('sequelize');
const Op = Sequelize.Op

// Get gig list
router.get('/', (req, res) => 
    Gig.findAll()
    // .then (giggs => {
        .then(documents => {
            // Creating an entire new Object named context with its own properties then pass in it into the render function will fix the issue...
            // https://stackoverflow.com/questions/59690923/handlebars-access-has-been-denied-to-resolve-the-property-from-because-it-is
            const context = {
              giggs: documents.map(document => {
                return {
                  title: document.title,
                  technologies: document.technologies,
                  budget: document.budget,
                  description: document.description,
                  contact_email: document.contact_email
                }
              })
            }
        
        res.render('gigs', {
            giggs: context.giggs,

        });
    })
    .catch(err => console.log(err)));

// Display add gig form
router.get('/add', (req, res) => res.render('add'));

// Add a gig
router.post('/add', (req, res) => {

    let { title, technologies, budget, description, contact_email } = req.body;

    let errors = []
    
    // Validation Fields
    if(!title) {
        errors.push({text: 'Please add a title'})
    }

    if(!technologies) {
        errors.push({text: 'Please add a technologies'})
    }

    if(!description) {
        errors.push({text: 'Please add a description'})
    }

    if(!contact_email) {
        errors.push({text: 'Please add a contact email'})
    }

    // Check for errors
    if(errors.length > 0) {
        res.render('add', {
            errors,
            title,
            technologies,
            budget,
            description,
            contact_email
        });
    } else {
        if(!budget) {
            budget = 'Unknown';
        } else {
            budget = `$${budget}`;
        }

        // Make lowercase and remove space after comma
        technologies =  technologies.toLowerCase().replace(/, /g, ',');
        // Insert into table
        Gig.create({
            title,
            technologies,
            description,
            budget,
            contact_email
        })
        .then(gig => res.redirect('/gigs'))
        .catch(err => console.log(err));
    }
});

// Search for gigs
router.get('/search', (req, res) => {
    let { term } = req.query

    // Make lowercase
    term = term.toLowerCase();
    
    Gig.findAll({ where: {technologies: { [Op.like]: '%' + term + '%'}}})
        // .then(giggs => res.render('gigs', {giggs})) # Creating an entire new Object named context with its own properties then pass in it into the render function will fix the issue (security update in sequelize v6)
        // .then( giggs => console.log(giggs))
        .then(documents => {
            const context = {
              giggs: documents.map(document => {
                return {
                    title: document.title,
                    technologies: document.technologies,
                    budget: document.budget,
                    description: document.description,
                    contact_email: document.contact_email
                }
              })
            }
            res.render('gigs', {
                giggs: context.giggs,
            });
        })
        .catch(err => console.log(err));
});

module.exports = router;