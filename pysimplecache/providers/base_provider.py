from abc import ABCMeta, abstractmethod


class UnhandledCachingException(Exception):
    """ Unhandled Caching Exception """

    def __init__(self, msg):
        self.message = msg


class BaseProvider(object):
    """ Base Caching Interface """

    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, key, ttl, method, **kwargs):
        """ Get cached data or call passed method

        :param key: str key value for cached data
        :param ttl: int ttl value for cached data
        :param method: obj method call for cache miss
        :param kwargs: parameters to pass into method
        :return: data, bool cache miss
        :raises: UnhandledCachingException
        """

    @abstractmethod
    def put(self, key, ttl, data):
        """ Put data into cache with passed ttl from referenced method

        :param key: str key value for cached data
        :param ttl: int ttl value for cached data
        :param data: data to pass into cache
        :return: None
        :raises: UnhandledCachingException
        """

    @abstractmethod
    def delete(self, key):
        """ Delete cached data with passed key

        :param key: str key value for cached data
        :return: None
        :raises: UnhandledCachingException
        """
