#!/bin/bash

ENDPOINT="http://13.62.103.104:5000/apidocs"

echo "Запуск хвилі $i..."
wrk -t8 -c500 -d5m $ENDPOINT/ >> ab_results.log
sleep 5