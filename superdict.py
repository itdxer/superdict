class SuperDict(dict):
    def __init__(self, data=None):
        if data is not None:
            for k, v in data.items():
                self[k] = SuperDict(v) if isinstance(v, dict) else v

    def __getattr__(self, attrname):
        if attrname not in self:
            self[attrname] = SuperDict()
        return self[attrname]

    def __setattr__(self, attrname, value):
        self[attrname] = value

    def __delattr__(self, attrname):
        del self[attrname]
