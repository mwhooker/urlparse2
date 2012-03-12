# encoding: utf-8
from recordtype import recordtype
urlparse1 = __import__('urlparse')

for name in (n for n in urlparse1.__dict__.iterkeys()):
    if name.startswith('__') or name == 'ParseResult':
        continue
    globals()[name] = getattr(urlparse1, name)


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
