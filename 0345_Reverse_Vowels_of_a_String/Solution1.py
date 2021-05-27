class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s = list(s)
        vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while l < r:
            while l < r and s[l] not in vowel_set:
                l += 1
            while l < r and s[r] not in vowel_set:
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)


def test(test_name, s, expected):
    res = Solution().reverseVowels(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = 'hello'
    expected1 = 'holle'
    test('test1', s1, expected1)

    s2 = 'leetcode'
    expected2 = 'leotcede'
    test('test2', s2, expected2)
