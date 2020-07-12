import math

import functools
import sys


from shutil import rmtree

class Vector2d:
    typecode = 'd'  # 这是一个class attribute
    
    functools.lru_cache()
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def __iter__(self):
        # 使得vector称为iterable。unpack时会使用
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self) # 因为vector是iterable，*self就是x和y
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.math.typot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))