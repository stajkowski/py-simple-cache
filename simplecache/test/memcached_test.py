import unittest
from simplecache.common.json_conversion import JsonConversion
from simplecache.providers.memcached import MemcachedProvider


class TestClass(object):

    def test_method(self, param1, param2):
        data = {
            'test1': 'value1',
            'test2': 'value2'
        }
        if param1 != 'p1' or param2 != 'p2':
            raise Exception('Unexpected error.')
        return data


class TestSetup(unittest.TestCase):
    """ Memcached Provider Test """

    def test_put_key_value(self):
        """ Test basic PUT key value """
        data = {
            'test1': 'value1',
            'test2': 'value2'
        }
        memcached = MemcachedProvider(JsonConversion(), servers='127.0.0.1')
        memcached.put('testkey1', 60, data)
        t = TestClass()

        # test local instance of memcached and ensure no
        # cache miss
        response, miss = memcached.get(
            'testkey1', 60, t.test_method, param1='p1', param2='p2')
        self.assertDictEqual(response, data)
        self.assertFalse(miss, msg='Unexpected cache miss.')

    def test_get_key_value_with_cache_miss(self):
        """ Test basic GET key with cache miss """
        data = {
            'test1': 'value1',
            'test2': 'value2'
        }
        memcached = MemcachedProvider(JsonConversion(), servers='127.0.0.1')
        t = TestClass()

        # test local instance of memcached with cache miss
        response, miss = memcached.get(
            'testkey2', 60, t.test_method, param1='p1', param2='p2')
        self.assertDictEqual(response, data)
        self.assertTrue(miss, msg='Unexpected cache hit.')

    def test_get_key_value_with_cache_miss_no_method(self):
        """ Test basic GET key with cache miss """
        memcached = MemcachedProvider(JsonConversion(), servers='127.0.0.1')

        # test local instance of memcached with cache miss
        response, miss = memcached.get('testkey3', 60, None)
        self.assertIsNone(response, msg='Unexpected value.')
        self.assertTrue(miss, msg='Unexpected cache hit.')

    def test_delete_key_with_expected_cache_miss(self):
        """ Test basic DELETE key with expected cache miss """
        data = {
            'test1': 'value1',
            'test2': 'value2'
        }
        memcached = MemcachedProvider(JsonConversion(), servers='127.0.0.1')
        memcached.put('testkey1', 60, data)
        memcached.delete('testkey1')
        t = TestClass()

        # test local instance of memcached and ensure no
        # cache miss
        response, miss = memcached.get(
            'testkey1', 60, t.test_method, param1='p1', param2='p2')
        self.assertDictEqual(response, data)
        self.assertTrue(miss, msg='Unexpected cache hit.')
