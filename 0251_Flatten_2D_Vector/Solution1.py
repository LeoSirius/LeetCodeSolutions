from typing import List

class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.flat = []
        for row in v:
            self.flat += row
        self.p = 0

    def next(self) -> int:
        res = self.flat[self.p]
        self.p += 1
        return res


    def hasNext(self) -> bool:
        return self.p < len(self.flat)



# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()

def test1():
    v = [[1,2],[3],[4]]
    obj = Vector2D(v)
    res1 = obj.next()    # 1
    res2 = obj.next()    # 2
    res3 = obj.next()    # 3
    res4 = obj.hasNext() # True
    res5 = obj.hasNext() # True
    res6 = obj.next()    # 4
    res7 = obj.hasNext() # False
    print("(res1, res2, res3, res4, res5, res6, res7) = {}".format((res1, res2, res3, res4, res5, res6, res7)))
    if (res1, res2, res3, res4, res5, res6, res7) == (1,2,3,True,True,4,False):
        print('test1 success.')
    else:
        print('test1 failed.')

if __name__ == "__main__":
    test1()


# Design and implement an iterator to flatten a 2d vector.
#  It should support the following operations: next and hasNext.

# Example:

# Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

# iterator.next(); // return 1
# iterator.next(); // return 2
# iterator.next(); // return 3
# iterator.hasNext(); // return true
# iterator.hasNext(); // return true
# iterator.next(); // return 4
# iterator.hasNext(); // return false

# Notes:

# Please remember to RESET your class variables declared in Vector2D, 
# as static/class variables are persisted across multiple test cases. 
# Please see here for more details.
# You may assume that next() call will always be valid, that is, 
# there will be at least a next element in the 2d vector when next() is called.
