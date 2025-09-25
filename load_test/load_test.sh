#!/bin/bash

ENDPOINT="http://51.20.109.42:5000/apidocs"

echo "Start testing..."
wrk -t8 -c500 -d5m $ENDPOINT/ >> ab_results.log
sleep 5