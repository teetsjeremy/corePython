

def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "{0} is equal to {1}".format(a, b)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):
    assert item not in collection, "{0} is in {1}".format(item, collection)

def test_between(upper_limit, lower_limit, actual):
    assert lower_limit <= actual <= upper_limit, "{2} is not between {1} and {0}".format(upper_limit, lower_limit, actual)

