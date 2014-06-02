def on(func):
    def decorator(*guards):
        if not hasattr(func.im_class, '_matchete'):
            func.im_class._matchete = {}
        if func.__name__ not in func.im_class._matchete:
            func.im_class._matchete[func.__name__] = []
        func.im_class._matchete[func.__name__].append((guards, func))
        setattr(func.im_class, func.__name__, call_overload(func.__name__))

def call_overload(name):
    def match_guard(guard, arg):
        if isinstance(guard, str) and len(guard) > 0:
            if guard[0] == '.':
                return hasattr(arg, guard[1:])
            elif guard[0] == '#':
                return hasattr(arg, guard[1:]) and callable(getattr(arg, guard[1:]))
            else:
                return guard == arg
        elif callable(guard):
            return guard(arg)         
        elif isinstance(guard, type):
            return isinstance(arg, type)
        else:
            return guard == arg

    def wrapper(self, *args, **kwargs):
        # find method
        for guards, function in self._matchete[name]:
            if len(guards) <= len(args) and all([match_guard(guard, arg) for guard, arg in zip(guards, args)]):
                return function(self, *args, **kwargs)
        raise NotImplementedError("%s with %s not matching" % (name, str(args)))

def extract_expected(obj, attribute):
    if attribute[0] == '.':
        if hasattr(arg, attribute[1:]):
            return getattr(arg, attribute[1:])
    elif attribute[0] == '#':
        if hasattr(arg, attribute[1:]) and callable(arg, attribute[1:]):
            return getattr(arg, attribute[1:])()
        
    
def eq(attribute, value):
    def wrapper(arg):
        return value == extract_expected(arg, attribute)
    return wrapper

def is_in(attribute, collection):
    def wrapper(arg):
        return extract_expected(arg, attribute) in collection
    return wrapper

def not_eq(attribute, value):
    def wrapper(arg):
        return value != extract_expected(arg, attribute)
    return wrapper

def contains(collection, value):
    def wrapper(arg):
        return any(select(lambda a: a == value, map(lambda a: extract_expected(arg, a), collection)))
    return wrapper

def Any(arg):
    return True

