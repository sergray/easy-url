import unittest

from easyurl import Query, URL


class TestQuery(unittest.TestCase):

    def test_empty_init(self):
        q = Query()
        self.assertEqual(str(q), '')
        q['a'] = 1
        q.update({'b': [2, '3']})
        q['c'] = [4]
        self.assertEqual(q['a'], 1)
        self.assertEqual(q['b'], [2, '3'])
        self.assertEqual(q['c'], 4)
        self.assertEqual(str(q), 'a=1&c=4&b=2&b=3')

    def test_init(self):
        q = Query('question=BIG&answer=some&answer=number')
        self.assertEqual(str(q), 'answer=some&answer=number&question=BIG')


class TestURL(unittest.TestCase):

    def test_init_read(self):
        u = URL('http://example.net')
        self.assertEqual(u.scheme, 'http')
        self.assertEqual( u.netloc, 'example.net')
        self.assertEqual(u.path,  '')
        self.assertEqual(u.params,  '')
        self.assertTrue(isinstance(u.query, Query))
        self.assertEqual(u.fragment,  '')
        self.assertEqual(str(u), 'http://example.net')

    def test_len(self):
        u = URL('')
        self.assertEqual(len(u), 6)

    def test_change(self):
        u = URL('http://example.net')
        u.scheme = 'https'
        u.netloc = 'user@example.org'
        u.path = 'library/search'
        u.query.update({'author': 'Douglas Adams',
            'isbn': ['0345391802', 9780345391834]})
        u.params = '0,146'
        u.fragment = 'books'
        self.assertEqual(str(u), 
            'https://user@example.org/library/search;0,146?'
            'isbn=0345391802&isbn=9780345391834&author=Douglas+Adams#books')
