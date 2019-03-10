from abc import ABCMeta, abstractmethod


class BaseConversion(object):
    """ Base Data Conversion Interface """

    __metaclass__ = ABCMeta

    @abstractmethod
    def encode(self, data):
        """ Encode passed data

        :param data: obj data
        :return: obj encoded data
        """

    @abstractmethod
    def decode(self, data):
        """ Decode passed data result

        :param data: obj data
        :return: obj decoded data
        """
