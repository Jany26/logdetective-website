"""Lyney would approve this :magic:"""

from src.spells import test_something


def sort_by_name(item):
    return item["name"]


def test_some_input():
    assert test_something(5) == 10
