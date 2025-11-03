class Omnibus():
    attr_count = {}

    def __setattr__(self, name, value):
        if name.startswith('_'):
            return super().__setattr__(name)
        else:
            super().__setattr__('_' + name, True) #inner mark
            if name in Omnibus.attr_count:
                Omnibus.attr_count[name] += 1
            else:
                Omnibus.attr_count[name] = 1

    def __getattribute__(self, name):
        if name.startswith('_'):
            return super().__getattribute__(name)
        else:
            return Omnibus.attr_count.get(name, 0)

    def __delattr__(self, name):
        if name.startswith('_'):
            return super().__delattr__(name)
        else:
            if name in Omnibus.attr_count and hasattr(self, '_'+name):
                super().__delattr__('_'+name)
                Omnibus.attr_count[name] -= 1
                if Omnibus.attr_count[name] == 0:
                    del Omnibus.attr_count[name]

import sys

inp = sys.stdin.read()
exec(inp)