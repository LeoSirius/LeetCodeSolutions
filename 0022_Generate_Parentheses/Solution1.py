from typing import List

class Solution:
    def gen(self, l, r, path, res):
        if l == 0 and r == 0:
            res.append(path)
            return
        if l: self.gen(l-1, r+1, path+'(', res)
        if r: self.gen(l, r-1, path+')', res)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.gen(n, 0, '', res)
        return res

def test(test_name, n, expected):
    res = Solution().generateParenthesis(n)
    if sorted(res) == sorted(expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 3
    expected1 = [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]
    test("test1", n1, expected1)
