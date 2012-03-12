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
