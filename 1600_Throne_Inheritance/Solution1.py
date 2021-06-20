from typing import *
from collections import defaultdict


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = kingName
        self.d_set = set()
        self.tree = defaultdict(list)

    def birth(self, parentName: str, childName: str) -> None:
        self.tree[parentName].append(childName)

    def death(self, name: str) -> None:
        self.d_set.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []
        def pre_order(name):
            if name not in self.d_set:
                res.append(name)
            for child_name in self.tree[name]:
                pre_order(child_name)
        pre_order(self.root)
        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

def test1():
    obj = ThroneInheritance('king')
    obj.birth('king', 'andy')
    obj.birth('king', 'bob')
    obj.birth('king', 'catherine')
    obj.birth('andy', 'matthew')
    obj.birth('bob', 'alex')
    obj.birth('bob', 'asha')
    res1 = obj.getInheritanceOrder()  # ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
    obj.death('bob')
    res2 = obj.getInheritanceOrder() # ["king", "andy", "matthew", "alex", "asha", "catherine"]
    print(f'res1 = {res1}')
    print(f'res2 = {res2}')

    if (res1 == ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"] and
            res2 == ["king", "andy", "matthew", "alex", "asha", "catherine"]):
        print('test1 succeed')
    else:
        print('test1 failed')


if __name__ == '__main__':
    test1()
