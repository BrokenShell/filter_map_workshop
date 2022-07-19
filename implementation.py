""" This file shows possible implementations for map and filter.
These are not the actual implementations, but they give us a good idea of how to
think about them. In reality these are implemented in c or c++ for Python.

Do not use this code in your projects. Use the real deal instead. """
from typing import Iterator, Iterable, Callable, Any


def my_map(transform: Callable[[Any], Any],
           iterable: Iterable[Any]) -> Iterator[Any]:
    return (transform(n) for n in iterable)


def my_filter(predicate: Callable[[Any], bool],
              iterable: Iterable[Any]) -> Iterator[Any]:
    return (n for n in iterable if predicate(n))
