echo "Running test load times...\n"
echo "\n\n\n-------[ LOAD TIMES ]-------\n"
if [ $1 = "crash" ]
then
    k6 run --vus 10000 --duration 30s automation/testload.js
else
    k6 run --vus 10 --duration 30s automation/testload.js
fi
echo "Running test load distribution...\n"
echo "\n\n\n-------[ LOAD DISTRIBUTION ]-------\n
python3 automation/testload.py