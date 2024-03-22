from dataclasses import dataclass
from enum import Enum

import redis

from src.serializer import RedisSerializer

# Initialize redis and serializer
rserial = RedisSerializer()
r = redis.Redis(host="localhost", port=6379, db=0)


class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


@dataclass
class StructuredData:
    value: int
    enum_value: Color


# Create classful and classless data for input
data = {"name": "John Doe", "age": 30, "city": "New York"}
structed_data = StructuredData(value=1, enum_value=Color.BLUE)

serialized_data = rserial.serialize(item=data)
serialized_structured_data = rserial.serialize(item=structed_data)

# Store the serialized data in a Redis hash
r.hset("user_data", "user_info", serialized_data)
r.hset("user_structed_data", "user_info", serialized_structured_data)


# Retrieve the serialized data from the Redis hash
redis_serialized_data = r.hget("user_data", "user_info")
redis_serialized_structed_data = r.hget("user_structed_data", "user_info")


# Deserialize the data from our serializer
deserialized_data = rserial.deserialize(redis_serialized_data)
deserialized_structured_data = rserial.deserialize(redis_serialized_structed_data)


print(deserialized_data)
print(deserialized_structured_data)
