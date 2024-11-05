#!/bin/bash

curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://0.0.0.0:8000/divide/1/2 -o divide_response.json
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://0.0.0.0:8000/multiply/1/20 -o multiply_response.json

