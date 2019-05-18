# Simple Caching Library for Python
[![Build Status](https://travis-ci.org/stajkowski/py-simple-cache.svg?branch=master)](https://travis-ci.org/stajkowski/py-simple-cache)

# Summary
Simple caching library for supported providers.  Pass method call to caching provider along with
generated key to populate memcached with the result.  The results will be returned with a boolean value
if there was a cache miss to assist in any metrics generation.

# Versions
0.0.1 - Support for memcached and json conversion

# Getting Started
1. Instantiate the provider:
   ```python
   from pysimplecache.common.json_serializer import JsonSerializer
   from pysimplecache.providers.memcached import MemcachedProvider

   memcached = MemcachedProvider(JsonSerializer(), servers='127.0.0.1')
   ```
2. PUT data into Memcached:
   ```python
       
   data = {
       'test1': 'value1',
       'test2': 'value2'
   }
   
    memcached.put('testkey1', 60, data) 
   ```
3. GET data by key from provider.  Optionally: Pass a method for a cache miss to load
data into provider from the result.

   ```python
    class TestClass(object):
    
        def test_method(self, param1, param2):
            data = {
                'test1': 'value1',
                'test2': 'value2'
            }
            if param1 != 'p1' or param2 != 'p2':
                raise Exception('Unexpected error.')
            return data
    
    t = TestClass()
    
    # test local instance of memcached with cache miss
    response, miss = memcached.get(
        'testkey2', 60, t.test_method, param1='p1', param2='p2')
   ```
4. DELETE data by key from provider.
   ```python
    memcached.delete('testkey1')
   ```