from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num2alpha = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = ['']
        for digit in digits:
            cur_str = num2alpha[int(digit)]
            tmp = []
            for row in res:
                for ch in cur_str:
                    tmp.append(row + ch)
            res = tmp
        return res



def test(test_name, digits, expected):
    res = Solution().letterCombinations(digits)
    if sorted(res) == sorted(expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    digits1 = "23"
    expected1 = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    test("test1", digits1, expected1)

    digits2 = ""
    expected2 = []
    test("test2", digits2, expected2)