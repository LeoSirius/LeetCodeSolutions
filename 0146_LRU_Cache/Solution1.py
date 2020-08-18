from collections import deque


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        self.head = ListNode()  # 最不常用的放在head后面
        self.tail = ListNode()  # 最近一次用过的结点放在tail前面

        self.head.next = self.tail
        self.tail.pre = self.head

    def move_node_to_tail(self, key):
        node = self.hashmap[key]
        # 把node从双向链表中移出来
        node.pre.next = node.next
        node.next.pre = node.pre

        # 把node放到tail前面
        node.pre = self.tail.pre
        node.next = self.tail

        self.tail.pre.next = node
        self.tail.pre = node


    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        self.move_node_to_tail(key)
        return self.hashmap[key].value


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_node_to_tail(key)
            return

        # 已经满了，则把head后面那个pop掉
        if len(self.hashmap) == self.capacity:
            self.hashmap.pop(self.head.next.key)
            self.head.next = self.head.next.next
            self.head.next.pre = self.head
        new_node = ListNode(key, value)
        self.hashmap[key] = new_node

        new_node.pre = self.tail.pre
        new_node.next = self.tail

        self.tail.pre.next = new_node
        self.tail.pre = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def test1():
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    res1 = obj.get(1)   # 1
    obj.put(3, 3)       # left 3, 1
    res2 = obj.get(2)   # -1
    obj.put(4, 4)       # left 4, 3
    res3 = obj.get(1)   # -1
    res4 = obj.get(3)   # 3
    res5 = obj.get(4)   # 4
    if (res1, res2, res3, res4, res5) == (1, -1, -1, 3, 4):
        print('test1 success.')
    else:
        print('test1 failed.')


def test2():
    obj = LRUCache(3)
    obj.put(1,1)
    obj.put(2,2)
    obj.put(3,3)
    obj.put(4,4)
    res1 = obj.get(4)  # 4
    res2 = obj.get(3)  # 3
    res3 = obj.get(2)  # 2
    res4 = obj.get(1)  # -1
    obj.put(5,5)
    res5 = obj.get(1)  # -1
    res6 = obj.get(2)  # 2
    res7 = obj.get(3)  # 3
    res8 = obj.get(4)  # -1
    res9 = obj.get(5)  # 5
    if (res1, res2, res3, res4, res5, res6, res7, res8, res9) == (
        4, 3, 2, -1, -1, 2, 3, -1, 5
    ):
        print('test2 success.')
    else:
        print('test2 failed.')


if __name__ == "__main__":
    test1()
    test2()


# Design and implement a data structure for Least Recently Used (LRU) cache. 
# It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key 
# if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. 
# When the cache reached its capacity, it should invalidate the least recently 
# used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
