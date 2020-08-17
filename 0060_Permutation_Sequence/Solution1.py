class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fac = [1]                                           # 阶乘的list，fac[i] = i!
        for i in range(1, n + 1):
            fac.append(fac[i-1] * i)

        num_char = ''.join(str(i+1) for i in range(n))      # num_char 存放字符，如n=4，则num_char = '1234'

        res = ''
        k -= 1
        for i in range(n - 1, -1, -1):
            idx = k // fac[i]
            k -= fac[i] * idx

            res += num_char[idx]
            num_char = num_char[:idx] + num_char[idx+1:]

        return res



def test(test_name, n, k, expected):
    res = Solution().getPermutation(n, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    n1, k1, expected1 = 3, 3, "213"
    test('test1', n1, k1, expected1)

    n2, k2, expected2 = 4, 9, "2314"
    test('test2', n2, k2, expected2)


# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。

# 说明：

# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 示例 1:

# 输入: n = 3, k = 3
# 输出: "213"
# 示例 2:

# 输入: n = 4, k = 9
# 输出: "2314"

