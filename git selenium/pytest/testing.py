import pytest

def setup_module(module):
    print('first')


def teardown_module(module):
    print('last')

def setup_function(function):
    print('lauching browser')

def teardown_function(function):
    print("exiting browser")

def testone():
    print('test1')


def test_two():
    print('test2')