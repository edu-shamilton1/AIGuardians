#!/bin/bash

### build steps
if [ "$1" == "build" ]
then
  echo "rebuilding..."
  cd frontend
  npm install
  npm run build
  cd ../
  docker compose build
fi

#export OPENAI_API_KEY="your API key"  # only set either OPENAI_API_KEY or GOOGLE_API_KEY not both.
#export GOOGLE_API_KEY="your API key"  # only set either OPENAI_API_KEY or GOOGLE_API_KEY not both.

echo "Starting..."
docker compose up

