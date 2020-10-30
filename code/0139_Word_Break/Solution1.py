from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]


def test(test_name, s, wordDict, expected):
    res = Solution().wordBreak(s, wordDict)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    s1 = 'leetcode'
    wordDict1 = ["leet", "code"]
    expected1 = True
    test('test1', s1, wordDict1, expected1)

    s2 = 'applepenapple'
    wordDict2 = ["apple", "pen"]
    expected2 = True
    test('test2', s2, wordDict2, expected2)

    s3 = 'catsandog'
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    expected3 = False
    test('test3', s3, wordDict3, expected3)
