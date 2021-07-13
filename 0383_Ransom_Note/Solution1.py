from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1, c2 = Counter(ransomNote), Counter(magazine)
        for ch, v in c1.items():
            if ch not in c2 or c2[ch] < v:
                return False
        return True


def test(test_name, ransomNote, magazine, expected):
    res = Solution().canConstruct(ransomNote, magazine)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    ransomNote1 = 'a'
    magazine1 = 'b'
    expected1 = False
    test('test1', ransomNote1, magazine1, expected1)

    ransomNote2 = 'aa'
    magazine2 = 'ab'
    expected2 = False
    test('test2', ransomNote2, magazine2, expected2)

    ransomNote3 = 'aa'
    magazine3 = 'aab'
    expected3 = True
    test('test3', ransomNote3, magazine3, expected3)
