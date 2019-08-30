class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(my_dict[digits[0]])
        else:
            prev = self.letterCombinations(digits[:-1])
            additional = list(my_dict[digits[-1]])
            return [x + y for x in prev for y in additional]