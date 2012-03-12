import urlparse2
from unittest import TestCase


class TestUsability(TestCase):

    def test_mutability(self):
        url = 'http://www.cwi.nl:80/%7Eguido/Python.html'
        expect = 'https://www.cwi.nl:80/%7Eguido/Python.html'

        result = urlparse2.urlparse(url)
        result.scheme = 'https'

        joined = urlparse2.urlunparse(result)
        self.assertEquals(joined, expect)

    def test_protocolless_urlprefix(self):
        prefix = 'domain.com'
        path = 'path/to/file'
        expect = 'domain.com/path/to/file'

        result = urlparse2.urljoin(prefix, path)
        self.assertEquals(result, expect)

    def test_protocolfull_urlprefix(self):
        prefix = 'http://domain.com'
        path = 'path/to/file'
        expect = 'http://domain.com/path/to/file'

        result = urlparse2.urljoin(prefix, path)
        self.assertEquals(result, expect)
