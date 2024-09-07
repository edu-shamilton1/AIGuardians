# AIGuardians
GovHack 2024

# Setup, Build and Start
Either go to https://aistudio.google.com/ and get a free API Key, or go to https://platform.openai.com/ and get an API key.
Install docker desktop for your operating system.
```
docker compose build
export [GOOGLE/OPENAI]_API_KEY="your API key"  # only set either OPENAI_API_KEY or GOOGLE_API_KEY not both.
docker compose up
```
visit http://localhost:3001/
