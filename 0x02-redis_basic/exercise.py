#!/usr/bin/env python3
""" Module contains the Cache class"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """Cache class for storing data in Redis"""

    def __init__(self) -> None:
        """Initialize the Cache instance with a Redis client and flush db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a randomly generated key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None
            ) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis using the provided key"""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """Retrieve a string from Redis using the provided key"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve an integer from Redis using the provided key"""
        return self.get(key, int)
