# encoding: utf-8
from uml_test import A, D, test


class E(D):
    def __init__(self):
        pass


class F(A, E):
    # don't need A
    def __init__(self):
        pass


def test_2():
    return test()
