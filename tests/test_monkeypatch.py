import sys


def test_urlparse_already_loaded():
    import urlparse
    import urlparse2

    assert urlparse.ParseResult is not urlparse2.ParseResult, "it is"
    del sys.modules['urlparse']
    del sys.modules['urlparse2']


def test_urlparse_not_already_loaded():
    import urlparse2
    import urlparse

    assert urlparse.ParseResult is not urlparse2.ParseResult, "it is"
    del sys.modules['urlparse']
    del sys.modules['urlparse2']
