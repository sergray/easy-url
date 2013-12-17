import urlparse, urllib

__all__ = ['Query', 'URL']


class Query(object):
    """ Parses passed query string with urlparse.parse_qs and provides
    mapping methods for updating query parameters.

    Interpolates query with urllib.urlencode.
    """

    __slots__ = ('params', )

    def __init__(self, query=''):
        self.params = urlparse.parse_qs(query)
        
    def __str__(self):
        return urllib.urlencode(self.params, doseq=True)
    
    def __getitem__(self, item):
        val = self.params[item]
        if isinstance(val, list) and len(val) == 1:
            return val[0]
        else:
            return val
    
    def __setitem__(self, item, val):
        if not isinstance(val, list):
            val = [val]
        self.params[item] = val
        
    def update(self, mapping):
        # TODO validation of values in mapping, they must not be nested mappings
        self.params.update(mapping)


class URL(object):
    """Parses passed URL with urlparse.urlparse, exposes writable
    attributes named after urlparse.ParseResult fields:    
    - scheme
    - netloc
    - path
    - params
    - query
    - fragment
    
    query attribute is Query instance.
    """
    
    __slots__ = urlparse.ParseResult._fields

    def __init__(self, url):
        self.scheme, self.netloc, self.path, self.params, query, self.fragment = urlparse.urlparse(url)
        self.query = Query(query)
    
    def __str__(self):
        return urlparse.urlunparse(str(s) for s in self)
    
    def __iter__(self):
        for field in urlparse.ParseResult._fields:
            yield getattr(self, field)
            
    def __len__(self):
        return len(urlparse.ParseResult._fields)
