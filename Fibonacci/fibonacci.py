from functools import wraps, cache
import sys

@cache
def fibonacci(n:int) -> int:
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci (n-2)
