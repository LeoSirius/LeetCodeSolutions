from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prototype = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in prototype:
                prototype[sorted_str].append(s)
            else:
                prototype[sorted_str] = [s]
        res = []
        for k, v in prototype.items():
            res.append(v)
        return res


def test(test_name, strs, expected):
    res = [sorted(item) for item in Solution().groupAnagrams(strs)]
    expected = [sorted(item) for item in expected]
    if (sorted(res) == sorted(expected)):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')
    

if __name__ == "__main__":
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected1 = [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
    ]
    test('test1', strs1, expected1)
