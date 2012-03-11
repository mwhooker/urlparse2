import urlparse as urlparse1



class Result(object):
    __slots__ = ('scheme', 'netloc', 'path', 'params', 'query', 'fragment')

    def __init__(self, scheme=None, netloc=None, path=None, params=None, query=None, fragment=None, urllib_pr=None):
        if not urllib_pr and isinstance(scheme, ParseResult):
            urllib_pr = scheme
        if urllib_pr:
            self.scheme = urllib_pr.scheme
            self.netloc = urllib_pr.netloc
            self.path = urllib_pr.path
            self.params = urllib_pr.params
            self.query = urllib_pr.query
            self.fragment = urllib_pr.fragment
        else:
            self.scheme = scheme
            self.netloc = netloc
            self.path = path
            self.params = params
            self.query = query
            self.fragment = fragment

    def _to_tuple(self):
        return (self.scheme, self.netloc, self.path, self.params, self.query, self.fragment)

    def to_urlparse(self):
        return urlparse1.ParseResult(*self._to_tuple())

    @staticmethod
    def from_urlparse(pr):
        return ParseResult(urllib_pr=pr)
    
    def geturl(self):
        raise NotImplemented

class SplitResult(Result):

    def geturl(self):
        return urlunsplit(self)

class ParseResult(Result):

    def geturl(self):
        return urlunparse(self)

def urlparse(url):
    return ParseResult.from_urlparse(urlparse1.urlparse(url))

def urlunparse(pr):
    return urlparse1.urlunparse(pr._to_tuple())
