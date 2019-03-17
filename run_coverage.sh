coverage run --source='./pysimplecache' --omit="*__init__*,*/test*" -m unittest discover -s pysimplecache/test -p '*_test.py'
coverage report -m
rm -rf ./htmlcov/*
coverage html
