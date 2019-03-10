echo "----------------------------------------"
echo "Running Build --------------------------"
echo "----------------------------------------"
python setup.py sdist bdist_wheel
python3 setup.py sdist bdist_wheel

python3 -m twine upload dist/*