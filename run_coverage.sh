coverage run --source='./simplecache' --omit="*__init__*,*/test*" -m unittest discover -s simplecache/test -p '*_test.py'
coverage report -m
rm -rf ./htmlcov/*
coverage html
