var express = require('express');
var router = express.Router();
var logger = require('morgan');



/* POST simple text summary test. */
router.post('/queryLLM', async function(req, res, next) {
    let question = req.body.queryText;
    
    //console.log(`[DEBUG] query question: ${question}`);
    const response = await fetch("http://llm:8080/summary/invoke", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "input" :
                {
                    "method": question
                }
            }
        ),
    });
    let retResponse = await response.json();
    //console.log(retResponse);
    res.json(retResponse.output.content);
  });
  

module.exports = router;
