from xbmcswift2.common import unpickle_args
import urlparse
try:
    from urlparse import parse_qs
except ImportError:
    from cgi import parse_qs


class Request(object):
    # TODO: no need for a class, use NamedTuple instead

    def __init__(self, url, handle):
        # TODO: combine argv0 and argtv1 then use urlparse to get the query
        # string before passing to parse_qs
        self.url = url
        self.handle = int(handle)

        # urlparse doesn't like the 'plugin' scheme, so pass a protocol
        # relative url, e.g. //plugin.video.helloxbmc/path
        self.scheme, remainder = url.split(':', 1)
        parts = urlparse.urlparse(remainder)
        _, self.netloc, self.path, self.query_string = parts[0], parts[1], parts[2], parts[4]
        self.args = unpickle_args(parse_qs(self.query_string))
