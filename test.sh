#!/bin/bash


## LLM tests

echo "Test User Profile"
curl "http://localhost:3001/user/getUserProfileList?postcode=2179"
echo ""
curl  -d "@a.json" -H "Content-type: application/json" "http://localhost:3001/user/getUserServicesList"
echo ""

echo  "Test LLM"

echo "1. Summarise text"
curl -d "@b.json" -H 'Content-type: application/json' "http://localhost:3001/llm/summariseText"

echo ""
echo "2. Translate text"
curl -d "@b.json" -H 'Content-type: application/json' "http://localhost:3001/llm/translateText"

# something wrong with input fields
echo ""
#echo "3. Query"
#curl -d "@c.json" -H 'Content-type: application/json' "http://localhost:3001/llm/queryLLM"

echo ""
echo "Test Telemetry data"
curl "http://localhost:3001/getTelementryData"

echo ""
