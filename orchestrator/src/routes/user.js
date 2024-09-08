var express = require('express');
var logger = require('morgan');

var fs = require('fs'); 


var csvData=[];
//var parser = parse({delimiter: ','});
/*
fs.createReadStream("Postcode SA2 mapping.csv")
    .pipe(parse({delimiter: ','}))
    .on('data', function(csvrow) {
        console.log(csvrow);
        //do something with csvrow
        csvData.push(csvrow);        
    })
    .on('end',function() {
      //do something with csvData
      console.log(csvData);
    });
*/

module.exports = function factory(telementyData) {
  const router = require('express').Router();

  /* GET user profile list. */
  router.get('/getUserProfileList', function(req, res, next) {
    let postCode = req.query.postcode;
    console.log(`[DEBUG] lookup postcode: ${postCode}`);
    var retProfile = {languageGroups: ["en-AU","ar","zh","pa"], SA2Block: {id: "115011558", name: "Cherrybrook"}};

    telementyData.push({timestamp: Date(), userProfile: {}, task: "postcode"});
    res.json(retProfile);
  });


  /* GET user services list */
  router.post('/getUserServicesList', function(req,res,next) {
    let profile = req.body.profile;
    console.log(`[DEBUG] use profile: ${profile}`);
    var retList = {services: [{serviceName: "Citizenship pathways", description: "Ask questions about pathsways to citizenship"},{serviceName: "Potholes", description: "Register a pothole near you"}, {serviceName: "Plain Speech", description: "Review a document into plain speech following Australian Style Manual"}]};

    telementyData.push({timestamp: Date(), userProfile: {}, task: "services"});
    res.json(retList);
  });

  return router;
}


//module.exports = router;
