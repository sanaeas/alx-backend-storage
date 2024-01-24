#!/usr/bin/env python3
""" Module that gets the content of a url"""
import requests
import redis
from typing import Callable
from functools import wraps


def count_and_cache(method: Callable) -> Callable:
    """Cache the output of data fetched from url"""
    @wraps(method)
    def wrapper(url) -> str:
        """Wrapper function caches the output"""
        r = redis.Redis()

        r.incr(f"count:{url}")

        cached_result = r.get(url)
        if cached_result:
            return cached_result.decode("utf-8")
        page_content = method(url)
        r.setex(f"result:{url}", 10, page_content)
        return page_content

    return wrapper


@count_and_cache
def get_page(url: str) -> str:
    """Get the content of a url"""
    response = requests.get(url)
    return response.text
