from collections import defaultdict
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        ch2freq = defaultdict(int)
        for i in s:
            ch2freq[i] += 1
        hp = []  # store [(-freq, ch)...]

        # len(s)恰好是 ch个数 * ch频率
        for ch in ch2freq:
            for i in range(ch2freq[ch]):
                # Python heapq默认是小顶堆，存负数，就变成大顶堆了
                # sort会自动按照tuple的第一个元素sort
                heapq.heappush(hp, (-ch2freq[ch], ch))

        return ''.join([heapq.heappop(hp)[1] for _ in range(len(s))])


def test(test_name, s, expected):
    res = Solution().frequencySort(s)
    if res in expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    s1 = "tree"
    expected_strs1 = ['eert']
    test('test1', s1, expected_strs1)

    s2 = 'cccaaa'
    expected_strs2 = ['cccaaa', 'aaaccc']
    test('test2', s2, expected_strs2)

    s3 = 'Aabb'
    expected_strs3 = ['bbAa']
    test('test3', s3, expected_strs3)

# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input:
# "cccaaa"

# Output:
# "cccaaa"

# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:

# Input:
# "Aabb"

# Output:
# "bbAa"

# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

