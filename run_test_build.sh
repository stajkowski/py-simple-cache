echo "----------------------------------------"
echo "Running Test Build --------------------------"
echo "----------------------------------------"
python setup.py sdist bdist_wheel
python3 setup.py sdist bdist_wheel

python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*