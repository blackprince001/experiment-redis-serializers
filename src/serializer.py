import pickle
from typing import List


class RedisSerializer:
    def __init__(self):
        self._first_variable = None

    @staticmethod
    def serialize(item: object, iterable: List[any] = None) -> bytes:
        # TODO handle redis-lists with iterables
        return pickle.dumps(item)

    @staticmethod
    def deserialize(obj_dump: any) -> any:
        # TODO handle redis-lists with iterables
        return pickle.loads(obj_dump)

    # TODO handle other redis data types.


# TODO make this repo a package to be reused anywhere.
# TODO add support for protobuf encoding schemes
