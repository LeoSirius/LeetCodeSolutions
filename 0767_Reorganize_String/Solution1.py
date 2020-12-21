from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        res = ''
        counter = Counter(S)

        # 边界条件：
        # 长度偶数的时候，大于一半
        # 长度基数的时候，大于一半加1
        # 加1是为了向上取整
        if max(counter.values()) > (len(S)+1) // 2:
            return res
        
        # 构建堆
        hp = []
        for ch, times in counter.items():
            heapq.heappush(hp, (-times, ch))
        
        prev = (0, None)   # prev是上次去掉的字母和其个数，
        while hp:
            times, ch = heapq.heappop(hp)
            res += ch
            if prev[0] < 0:
                heapq.heappush(hp, prev)
            prev = (times+1, ch)         # python用负数做key来构建最大堆。heapq默认是最小堆

        return res


def test(test_name, S, exepcted):
    res = Solution().reorganizeString(S)
    if res == exepcted:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    S1 = "aab"
    expected1 = "aba"
    test('test1', S1, expected1)

    S2 = "aaab"
    expected2 = ""
    test('test2', S2, expected2)

    S3 = "aaababaacbb"
    expected3 = "ababababaca"
    test('test3', S3, expected3)


# Given a string S, check if the letters can be rearranged so 
# that two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, 
# return the empty string.

# Example 1:

# Input: S = "aab"
# Output: "aba"

# Example 2:

# Input: S = "aaab"
# Output: ""

# Note:

# S will consist of lowercase letters and have length in range [1, 500].


