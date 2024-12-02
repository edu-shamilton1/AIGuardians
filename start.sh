#!/bin/bash

### build steps
if [ "$1" == "build" ]
then
  echo "rebuilding..."
  cd frontend
  if [ ! -f ".env" ]
  then
    echo -e "Edit the .env file in the frontend folder before building"
    echo -e 'VITE_AI_API=http://localhost:3001\nVITE_TTS_KEY=\nVITE_TTS_REGION=australiaeast' >.env
    exit -1
  fi
  npm install
  npm run build
  cd ../
  docker compose build
fi

# use a .env file to store your API key, this must not be added to Git, and keeps this file clean.
if [ ! -f ./.env ]
then
  echo -e '#GOOGLE_API_KEY=""\n#OPENAI_API_KEY=""' >.env
  echo -e "Stopped\n Edit .env with either your Google AI Studio or OpenAI API key"
  exit -1
else
  . ./.env
fi

env | grep -i "API_KEY"

echo "Starting..."
docker compose up
