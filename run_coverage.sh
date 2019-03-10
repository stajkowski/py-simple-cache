coverage run --source='./simple-cache' --omit="*__init__*,*/test*" -m unittest discover -s simple-cache/test -p '*_test.py'
coverage report -m
rm -rf ./htmlcov/*
coverage html
