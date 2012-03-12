# encoding: utf-8
import sys
from recordtype import recordtype

import urlparse as urlparse1
from urlparse import *
del sys.modules['urlparse']


class ParseResult(recordtype('ParseResult', 'scheme netloc path params query fragment'), urlparse1.ResultMixin):

    __slots__ = ()

    def geturl(self):
        return urlparse1.urlunparse(self)


class SplitResult(recordtype('SplitResult', 'scheme netloc path query fragment'), urlparse1.ResultMixin):

    __slots__ = ()

    def geturl(self):
        return urlparse1.urlunsplit(self)


urlparse1.ParseResult = ParseResult
urlparse1.SplitResult = SplitResult


def urljoin(base, url, allow_fragments=True):
    parsed = urlparse1.urlparse(base)
    if not parsed.scheme or not parsed.netloc:
        raise ValueError("Invalid base url")
    return urlparse1.urljoin(base, url, allow_fragments=allow_fragments)
