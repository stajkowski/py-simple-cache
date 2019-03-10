import bmemcached
import os
from simplecache.providers.base_provider import BaseProvider, \
    UnhandledCachingException


class MemcachedProvider(BaseProvider):
    """ Memcached Provider """

    def __init__(self, conversion, username=None, password=None,
                 servers=None, enabled=True):
        """ Memcached Provider

        :param conversion: class for data conversion
        :param username: str memcached username
        :param password: str memcached password
        :param servers: str memcached servers (comma separated)
        :param enabled: bool if caching is enabled
        """
        self.conversion = conversion
        self.cache_enabled = bool(os.getenv('MEMCACHEDCLOUD_ENABLED', enabled))
        self.cache_server = os.getenv('MEMCACHEDCLOUD_SERVERS', servers)
        self.cache_user = os.getenv('MEMCACHEDCLOUD_USERNAME', username)
        self.cache_pass = os.getenv('MEMCACHEDCLOUD_PASSWORD', password)
        self._client = self._setup_client()

    def _setup_client(self):
        """ Setup memcached client

        :return: obj memcached client
        """
        if self.cache_enabled:
            try:
                if self.cache_user and self.cache_pass:
                    return bmemcached.Client(
                        self.cache_server.split(','),
                        self.cache_user,
                        self.cache_pass)
                else:
                    return bmemcached.Client(
                        self.cache_server.split(','))
            except Exception as e:
                raise UnhandledCachingException(
                    'UnhandledCachingException: {}'.format(str(e.message)))

        return None

    def get(self, key, ttl, method, **kwargs):
        """ Get cached data or call passed method

        :param key: str key value for cached data
        :param ttl: int ttl value for cached data
        :param method: obj method call for cache miss
        :param kwargs: parameters to pass into method
        :return: data, bool cache miss
        :raises: UnhandledCachingException
        """
        if self._client:
            try:
                data = self._client.get(key)
                # if cache hit then return data decoded and if no
                # data present in cache, call method with passed
                # arguments and store in cache
                if data:
                    return self.conversion.decode(data), False
                else:
                    # if method is passed, load data and pass into
                    # memcached with key
                    if method is not None:
                        data = method(**kwargs)
                        self.put(key, ttl, data)
                        return data, True
                    else:
                        return None, True
            except Exception as e:
                raise UnhandledCachingException(
                    'UnhandledCachingException: {}'.format(str(e.message)))
            finally:
                self._client.disconnect_all()

    def put(self, key, ttl, data):
        """ Put data into cache with passed ttl from referenced method

        :param key: str key value for cached data
        :param ttl: int ttl value for cached data
        :param data: data to pass into cache
        :return: None
        :raises: UnhandledCachingException
        """
        if self._client:
            try:
                self._client.set(key, self.conversion.encode(data), ttl)
            except Exception as e:
                raise UnhandledCachingException(
                    'UnhandledCachingException: {}'.format(str(e.message)))
            finally:
                self._client.disconnect_all()

    def delete(self, key):
        """ Delete cached data with passed key

        :param key: str key value for cached data
        :return: None
        :raises: UnhandledCachingException
        """
        if self._client:
            try:
                self._client.delete(key)
            except Exception as e:
                raise UnhandledCachingException(
                    'UnhandledCachingException: {}'.format(str(e.message)))
            finally:
                self._client.disconnect_all()
