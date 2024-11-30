#!/bin/bash


## LLM tests

echo "Test User Profile"
curl "http://localhost:3001/user/getUserProfileList?postcode=2179"
echo ""

curl  -d "@a.json" -H "Content-type: application/json" "http://localhost:3001/user/getUserServicesList"
echo ""

echo -e  "\nTest LLM"

echo -e "\n1. Summarise text"
curl -d "@b.json" -H 'Content-type: application/json' "http://localhost:3001/llm/summariseText"
echo ""

echo -e "\n2. Translate text"
curl -d "@b.json" -H 'Content-type: application/json' "http://localhost:3001/llm/translateText"
echo ""

echo -e "\n3. Query"
curl -d "@c.json" -H 'Content-type: application/json' "http://localhost:3001/llm/queryLLM"
echo ""

echo -e "\n4. RAG query"
curl -d "@d.json" -H "Content-type: application/json" "http://localhost:3001/llm/queryContent"
echo ""

echo -e "\nTest Telemetry data"
curl "http://localhost:3001/getTelementryData"
echo ""
