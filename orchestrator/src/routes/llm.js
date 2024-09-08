var express = require('express');
var logger = require('morgan');


module.exports = function factory(telementyData) {
    const router = require('express').Router();
    const llmServer = "llm:8080";
    const languageNames = {"en":"english", "zh":"chinese", "pu": "punjabi", "ar": "arabic"}

    /* POST simple text summary test. */
    router.post('/queryLLM', async function(req, res, next) {
        let profile  = req.body.profile;
        let question = req.body.fullText;

        console.log(`[DEBUG] summarise: ${question}`);
        console.log(`[DEBUG] with profile: ${profile}`);
        
        const response = await fetch(`http://${llmServer}/queryLLM/invoke`, {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify({
                "input" :
                    {
                        "fullText": question
                    }
                }
            ),
        });
        let retResponse = await response.json();
        telementyData.push({timestamp: Date(), userProfile: profile, task: "queryLLM"})
        console.log(retResponse);
        res.json({"status": 200, "response": retResponse.output.content});
    });

    /* POST simple text summary test. */
    router.post('/summariseText', async function(req, res, next) {
        let profile  = req.body.profile;
        let question = req.body.fullText;

        console.log(`[DEBUG] summarise: ${question}`);
        console.log(`[DEBUG] with profile: ${profile}`);
        
        const response = await fetch(`http://${llmServer}/summarise/invoke`, {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify({
                "input" :
                    {
                        "fullText": question
                    }
                }
            ),
        });
        let retResponse = await response.json();

        telementyData.push({timestamp: Date(), userProfile: profile, task: "summariseText"})
        console.log(retResponse);
        res.json({"status": 200, "response": retResponse.output.content});
    });


    /* POST simple text summary test. */
    router.post('/translateText', async function(req, res, next) {
        let profile  = req.body.profile;
        let question = req.body.fullText;
        let newLanguage = languageNames[profile.selectedLanguage];

        console.log(`[DEBUG] translate: ${question} to ${newLanguage}`);
        console.log(`[DEBUG] with profile: ${profile}`);
        const response = await fetch(`http://${llmServer}/translate/invoke`, {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify({
                "input" :
                    {
                        "fullText": question,
                        "language": newLanguage
                    }
                }
            ),
        });
        let retResponse = await response.json();

        telementyData.push({timestamp: Date(), userProfile: profile, task: "translateText"})
        console.log(retResponse);
        res.json({"status": 200, "language": newLanguage, "response": retResponse.output.content});
    });


    return router;
};
  


