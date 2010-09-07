class LegacyView(object):
    def __init__(self, app):
        self.app = app # app is the legacy Pylons app

    def __call__(self, request):
        return request.get_response(self.app)
    
class action(object):
    def __init__(self, **kw):
        self.kw = kw

    def __call__(self, wrapped):
        if hasattr(wrapped, '__exposed__'):
            wrapped.__exposed__.append(self.kw)
        else:
            wrapped.__exposed__ = [self.kw]
        return wrapped
    