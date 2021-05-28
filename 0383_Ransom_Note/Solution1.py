class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        def c2zero(ch):
            return ord(ch)-ord('a')

        arr1, arr2 = [0] * 26, [0] * 26
        for i in range(len(magazine)):
            if i < len(ransomNote):
                arr1[c2zero(ransomNote[i])] += 1
            arr2[c2zero(magazine[i])] += 1
        for i in range(26):
            if arr1[i] > arr2[i]:
                return False
        return True


def test(test_name, ransomNote, magazine, expected):
    res = Solution().canConstruct(ransomNote, magazine)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


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
