# Router/Orchestrator

This is primary API interface from the front-end to the LLM services

# How to build and start
```
cd frontend
# create dist/ folder
npm run build
# return to parent folder
cd ../
docker build -f orchestrator/Dockerfile -t govhack-orchestrator:dev .
docker run -i -t -p 3001:3001 govhack-orchestrator:dev .
```



