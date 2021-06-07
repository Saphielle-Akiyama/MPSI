import functools
import operator as op
from typing import Optional

VALID_OPERATIONS = {
    "+": op.add,
    "-": op.sub,
    "@": op.matmul,
    "/": op.truediv,
    "//": op.floordiv,
    "**": op.pow,
    "%": op.mod,
    "<<": op.lshift,
    ">>": op.rshift,
    "&": op.and_,
    "^": op.xor,
    "|": op.or_,
}





class ComposableMeta(type):
    def __new__(cls, name: str, bases: tuple, dct: dict):
        composable = super().__new__(cls, name, bases, dct)

        for op_symbol, op in VALID_OPERATIONS.items():

            def fn(self, other):
                def ret(*args, **kwargs):
                    return op(self.inner(*args, **kwargs), other.inner(*args, **kwargs))

                return self.new(ret, other, op=op_symbol)

            setattr(composable, '__' + op.__name__.rstrip('_') + '__', lambda self, other: fn(self, other))

        return composable


class Composable(metaclass=ComposableMeta):
    def __init__(self, inner: callable, *, cmps: Optional[list] = None):
        self.inner = inner
        functools.update_wrapper(self, inner)

        self.cmps = cmps or [inner]

    # Infos
    
    def __len__(self) -> int:
        return len(self.cmps)

    def __iter__(self):
        for fn in self.cmps:
            if isinstance(fn, str):
                continue

            if self.is_self(fn):
                yield from fn.__iter__()

            else:
                yield fn

    def __contains__(self, obj) -> bool:
        for x in self:
            if x == obj:
                return True

        return False

    def __repr__(self) -> str:
        if len(self.cmps) == 1:
            return str(self.inner)
            
        return self.__class__.__name__ + '(' + ' '.join(map(str, self.cmps)) + ')'

    __str__ = __repr__

    # Actual operations
    
    def new(self, ret, other, *, op: str):
        return self.__class__(other, cmps=self.cmps + [op, other])
        
    def __matmul__(self, other):
        def ret(*args, **kwargs):
            return self.inner(other.inner(*args, **kwargs))

        return self.new(ret, other, op='@')

    def __call__(self, *args, **kwargs):
        return self.inner(*args, **kwargs)

@Composable
def identity(x):
    return x 

@Composable
def double(x):
    return 2 * x

@Composable
def triple(x):
    return 3 * x

@Composable
def square(x):
    return x ** 2

@Composable
def idk(x):
    return x

print((double + triple)(2))