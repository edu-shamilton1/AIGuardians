# Router Endpoints
Calls from front-end to orchestrator

## Object
** UserProfile **
```
{
  selectedLanguage: "zh-CH",
  inclusionFeatures: {tts: false, readinglevel: null, .. },
  userPostcode: "2179",
  userSA2: {id: "127011505", name: "Badgerys Creek - Greendale"}
}
```
## Dashboard Services
** /getTelementryData **
returns:
```

```
curl "http://localhost:3001/getTelementryData"

## User Services
** /user/getUserProfileList(postcode:string) **
returns:
```
{
 languageGroups: ["en-AU","ar","zh","pa"],
 SA2Block: {id: "115011558", name: "Cherrybrook"}
}
```
curl "http://localhost:3001/user/getUserProfileList?postcode=2179"


** /user/getUserServicesList(profile:userProfile) **
returns:
```
{
  services: [
    {serviceName: "Citizenship pathways", description: "Ask questions about pathsways to citizenship"},
    {serviceName: "Potholes", description: "Register a pothole near you"},
  ]
}
```
curl  -d '{"profile":{"selectedLanguage":"zh-CH","inclusionFeatures":{"tts":"false","readinglevel":""},"userPostcode":"2179","userSA2":{"id":"127011505","name":"Badgerys Creek - Greendale"}}}' -H "Content-type: application/json" "http://localhost:3001/user/getUserServicesList"


## LLM Backend Services

** /llm/queryLLM(profile:userProfile, queryText:string) **
returns:
```
{
 status: 200,
 response: "The word 'demonstrate' contains the word 'demon' at the beginning"
}
```
curl -d "@b.json" -H 'Content-type: application/json' "http://localhost:3001/llm/queryLLM


** /llm/translateText(profile:userProfile, text:string) **
returns:
```
{
  "status": 200,
  "language": "chinese",
  "response": "Response in new different language"
}
```
curl -d "@b.json" -H 'Content-type: application/json' "http://localhost:3001/llm/translateText"


** /llm/queryContent(profile:userProfile, task:string, text:string) **
returns:
```
{
}
```

** /llm/summariseText(profile:userProfile, text:string) **
returns:
```
{
  "status": 200,
  "response": "*Markdown*\nSome Markdown text"
}
```
curl -d "@b.json" -H 'Content-type: application/json' "http://localhost:3001/llm/summariseText"
where b.json looks like;
```
{
 "profile": {
   "selectedLanguage": "zh-CH",
   "inclusionFeatures": {
     "tts": "false", 
     "readinglevel": ""
   },
   "userPostcode": "2179",
   "userSA2": {
     "id": "127011505", "name": "Badgerys Creek - Greendale"
   }
 },
 "fullText": "Character requirements for Australian Citizenship\n​​​​​​​​​Overview\nApplicants for Australian citizenship aged 18 years and over must be of 'good character'. Good character generally refers to the 'enduring moral qualities of a person'. If a person is found to be of good character, then we have considered that they are likely to uphold and obey the laws of Australia and other commitments they make through the Australian Citizenship Pledge​.\nApplicants may need to give us a penal clearance certificate for countries visited outside Australia.​\nIn addition, any applicant for citizenship by conferral, regardless of age, must not be approved for citizenship in certain circumstances relating to criminal offences.\nNational Police Checking Service (NPCS)\nThe Australian Criminal Intelligence Commission (ACIC) works with Australian police agencies to deliver the National Police Checking Service (NPCS). The NPCS allows people to apply for a Nationally Coordinated Criminal History Check (NCCHC). A NCCHC is an important part of the assessment of your citizenship application."
}

```

