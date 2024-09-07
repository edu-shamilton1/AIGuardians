var express = require('express');
var router = express.Router();
var logger = require('morgan');


/* GET user profile list. */
router.get('/getUserProfileList', function(req, res, next) {
  let postCode = req.query.postcode;
  console.log(`[DEBUG] lookup postcode: ${postCode}`);
  var retProfile = {languageGroups: ["en-AU","ar","zh","pa"], SA2Block: {id: "115011558", name: "Cherrybrook"}};

  res.json(retProfile);
});


/* GET user services list */
router.get('/getUserServicesList', function(req,res,next) {
  let profile = req.query.profile;
  console.log(`[DEBUG] use profile: ${profile}`);
  var retList = {services: [{serviceName: "Citizenship pathways", description: "Ask questions about pathsways to citizenship"},{serviceName: "Potholes", description: "Register a pothole near you"}, {serviceName: "Plain Speech", description: "Review a document into plain speech following Australian Style Manual"}]};

  res.json(retList);
});


module.exports = router;
