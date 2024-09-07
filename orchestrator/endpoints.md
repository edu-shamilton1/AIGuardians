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

## User Services
** /user/getUserProfileList(postcode:string) **
returns:
```
{
 languageGroups: ["en-AU","ar","zh","pa"],
 SA2Block: {id: "115011558", name: "Cherrybrook"}
}
```

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


## LLM Backend Services

** /llm/queryLLM(profile:userProfile, queryText:string) **
returns:
```
{
 status: 200,
 query: "How many demons are there in demonstrate",
 response: "The word 'demonstrate' contains the word 'demon' at the beginning"
}
```

** /llm/translateText(profile:userProfile, text:string) **
returns:
```
{
}
```

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
}
```

