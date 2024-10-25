import redis
import uuid
from typing import Union

class Cache:
    def __init__(self):
        """Initialize the Cache with a Redis client instance and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis using a randomly generated key.
        
        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.
        
        Returns:
            str: The generated random key where the data is stored.
        """
        key = str(uuid.uuid4())  # Generate a unique key
        self._redis.set(key, data)  # Store data in Redis
        return key
