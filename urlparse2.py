import urlparse as urlparse1



class ParseResult(object):
    __slots__ = ['scheme', 'netloc', 'path', 'params', 'query', 'fragment']

    def __init__(self, scheme, netloc, path, params, query, fragment, urllib_pr=None):
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


    def to_urlparse(self):
        return urlparse1.ParseResult(

    @staticmethod
    def from_urlparse(pr):
        return ParseResult(urllib_pr=pr)
        pass

def urlparse(url):
    return ParseResult.from_urlparse(urlparse1.urlparse(url))

def urljoin(pr):
    pass
