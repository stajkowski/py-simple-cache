echo "----------------------------------------"
echo "Running Tests --------------------------"
echo "----------------------------------------"
python -m unittest discover -s simple-cache/test -p '*_test.py'

./run_pep8.sh
