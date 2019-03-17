import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysimplecache",
    version="0.0.1",
    author="Brian Stajkowski",
    author_email="stajkowski100@gmail.com",
    description="A simple caching library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stajkowski/simple-cache",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
