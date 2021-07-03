import pytest

# Wrting custom exception class


class NotInRnage(Exception):
    def __init__(self, message="value not in range"):
        self.message = message
        super().__init__(self.message)


# example of custome error. NOTE: add test_ before every function
def test_generic():
    # a=2
    # b=2
    #assert a!=b

    a = 5
    with pytest.raises(NotInRnage):
        if a not in range(10, 20):
            raise NotInRnage


def test_test2():
    a = 2
    b = 2
    if a == 2:
        assert True
