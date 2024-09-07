# Router Endpoints
Calls from front-end to orchestrator

## User Services
** getUserProfileList(postcode:string) **
returns:
```
{
 languageGroups: ["en-AU","ar","zh","pa"],
 SA2Block: {id: "115011558", name: "Cherrybrook"}
}
```

** getUserServicesList(profile:userProfile) **
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

** queryLLM(profile:userProfile, queryText:string) **
returns:
```
{
 status: 200,
 query: "How many demons are there in demonstrate",
 response: "The word 'demonstrate' contains the word 'demon' at the beginning"
}
```

** translateText(profile:userProfile, text:string) **
returns:
```
{
}
```

** queryContent(profile:userProfile, task:string, text:string) **
returns:
```
{
}
```

** summariseText(profile:userProfile, text:string) **
returns:
```
{
}
```
