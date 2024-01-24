#!/usr/bin/env python3
""" Module contains the Cache class"""
import redis
import uuid
from typing import Union


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
