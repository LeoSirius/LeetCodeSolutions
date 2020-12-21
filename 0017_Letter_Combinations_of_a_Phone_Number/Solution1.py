from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mp = {
            2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
        }
        res = ['']
        for i in digits:
            target_str = mp[int(i)]
            tmp = []
            for char in target_str:      # 这样写易读，当然也可以写得更简洁
                for row in res:
                    tmp.append(row + char)
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