import decimal
import json
from pysimplecache.common.base_serializer import BaseSerializer


class JsonSerializer(BaseSerializer):
    """ JSON Conversion Library """

    def encode(self, data):
        """ Encode passed data

        :param data: obj data
        :return: obj encoded data
        """
        return json.dumps(data, default=self._obj_default)

    def decode(self, data):
        """ Decode passed data result

        :param data: obj data
        :return: obj decoded data
        """
        return json.loads(data)

    def _obj_default(self, obj):
        """ Convert invalid object types to valid

        :param obj: obj
        :return: valid obj
        """
        if isinstance(obj, decimal.Decimal):
            decimal_value = float(obj) - int(obj)
            if decimal_value > 0:
                return float(obj)
            return int(obj)
        raise TypeError
