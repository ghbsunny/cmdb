from functools import partial
import inspect


def add(x, y, z):
    return x + y + z


newadd = partial(add, y=4)

print(inspect.signature(newadd))
print(newadd(6, z=7))
