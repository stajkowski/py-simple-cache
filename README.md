# Simple Caching Library for Python
[![Build Status](https://travis-ci.org/stajkowski/simple-cache.svg?branch=master)](https://travis-ci.org/stajkowski/simple-cache)

# Summary
Simple caching library for supported providers.  Pass method call to caching provider along with
generated key to gain the most flexibility.  The results will be returned with a boolean value
if there was a cache miss to assist in any metrics generation.