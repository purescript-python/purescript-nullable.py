null = None

def nullable(a,r,f):
    return r if (a is null) else f(a)

def notNull(x):
    return x;
