import urlparse, urllib

__all__ = ['Query', 'URL']


class Query(object):
    """ Parses passed query string with urlparse.parse_qs and provides
    mapping methods for updating query parameters.

    Interpolates query with urllib.urlencode.
    """

    def __init__(self, query=''):
        self._params = urlparse.parse_qs(query)

    def __repr__(self):
        return repr(self._params)
        
    def __str__(self):
        return urllib.urlencode(self._params, doseq=True)
    
    def __getitem__(self, item):
        val = self._params[item]
        if isinstance(val, list) and len(val) == 1:
            return val[0]
        else:
            return val
    
    def __setitem__(self, item, val):
        if not isinstance(val, list):
            val = [val]
        self._params[item] = val

    def __iter__(self):
        for k in self._params:
            yield self._params[k]

    def __len__(self):
        return len(self._params)

    def keys(self):
        return self._params.keys()
        
    def update(self, mapping):
        # TODO validation of values in mapping, they must not be nested mappings
        self._params.update(mapping)


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
    
    _fields = urlparse.ParseResult._fields

    def __init__(self, url):
        for field, value in zip(self._fields, urlparse.urlparse(url)):
            setattr(self, field, value)

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        if isinstance(value, Query):
            self._query = value
        else:
            self._query = Query(value)
    
    def __str__(self):
        return urlparse.urlunparse(str(s) for s in self)

    def __getitem__(self, field_idx):
        if isinstance(field_idx, slice):
            return [getattr(self, field) for field in self._fields[field_idx]]
        else:
            return getattr(self, self._fields[field_idx])

    def __setitem__(self, field_idx, val):
        if isinstance(field_idx, slice):
            for field in self._fields[field_idx]:
                setattr(self, field, val)
        else:
            setattr(self, self._fields[field_idx], val)

    def __iter__(self):
        for field in self._fields:
            yield getattr(self, field)
            
    def __len__(self):
        return len(self._fields)
