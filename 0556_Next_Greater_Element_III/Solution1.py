class Solution:
    def nextGreaterElement(self, n: int) -> int:
        stk = []
        n_str_list = list(str(n))
        idx = 0
        i = len(n_str_list)-1
        while i >= 0:
            # 当栈中有元素，且i位置的元素比栈顶的元素小（说明递减了），则pop出来，
            # 最下面再把i位置的元素push进栈
            # 这样保证了栈是递增的

            # 12443111,这时i指向2，stk里是[1,1,1,3]，最后，idx就是3
            while stk and n_str_list[i] < n_str_list[stk[-1]]:
                idx = stk.pop()

            # idx不为0，说明遇到了第一个从右到左递减的元素
            # 且idx是比i大的最小元素
            if idx:
                n_str_list[idx], n_str_list[i] = n_str_list[i], n_str_list[idx]
                break

            stk.append(i)
            i -= 1

        if idx == 0:
            return -1

        right = n_str_list[i+1:]
        right.reverse()
        n_str_list = n_str_list[:i+1] + right
        return int(''.join(n_str_list))


def test(test_name, n, expected):
    res = Solution().nextGreaterElement(n)
    print(f'res = {res}')
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 12
    expected1 = 21
    test('test1', n1, expected1)

    n2 = 21
    expected2 = -1
    test('test2', n2, expected2)

    n3 = 1244311
    expected3 = 1311244
    test('test3', n3, expected3)

    n4 = 12222333
    expected4 = 12223233
    test('test4', n4, expected4)


# Given a positive integer n, find the smallest integer which has exactly
#  the same digits existing in the integer n and is greater in value than n. 
#  If no such positive integer exists, return -1.

# Note that the returned integer should fit in 32-bit integer, 
# if there is a valid answer but it does not fit in 32-bit integer, return -1.


# Example 1:

# Input: n = 12
# Output: 21

# Example 2:

# Input: n = 21
# Output: -1
#  

# Constraints:

# 1 <= n <= 231 - 1


