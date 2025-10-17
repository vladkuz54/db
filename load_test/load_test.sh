#!/bin/bash

ENDPOINT="http://13.60.16.200:5000/apidocs"

echo "Start testing..."
wrk -t8 -c500 -d5m $ENDPOINT
sleep 5 