#!/bin/bash

ENDPOINT="http://13.60.169.201:5000/apidocs"

echo "Start testing..."
wrk -t8 -c500 -d5m $ENDPOINT/ >> ab_results.log
sleep 5