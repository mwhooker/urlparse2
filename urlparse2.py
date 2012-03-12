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


urlparse1.ParseResult = ParseResult
