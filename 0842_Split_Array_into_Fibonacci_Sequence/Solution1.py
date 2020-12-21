from typing import *

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        self.res = []
        def backtrack(p, tmp_list):
            if len(tmp_list) >= 3 and p == len(S):  # 只有在这种条件满足下，才有解，否则返回[]
                self.res = tmp_list
                return
            if p == len(S):
                return

            for i in range(p, len(S)):
                if S[p] == '0' and i > p: # 如果拆分的数不是0，且以0开头，则跳过。这是题目要求
                    return
                num = int(S[p:i+1])       # num就是当前拆分的数
                if num > 2**31-1 or num < 0:
                    return

                if len(tmp_list) < 2:
                    backtrack(i+1, tmp_list + [num])  # 小于2个时，直接添加
                    continue
                if num == tmp_list[-1] + tmp_list[-2]:
                    backtrack(i+1, tmp_list + [num])

        backtrack(0, [])
        return self.res


def test(test_name, S, expected_list_arr):
    res = Solution().splitIntoFibonacci(S)
    print(f'res = {res}')
    if res in expected_list_arr:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    S1 = '123456579'
    expected_list_arr1 = [[123,456,579]]
    test('test1', S1, expected_list_arr1)

    S2 = '11235813'
    expected_list_arr2 = [[1,1,2,3,5,8,13]]
    test('test2', S2, expected_list_arr2)

    S3 = '112358130'
    expected_list_arr3 = [[]]
    test('test3', S3, expected_list_arr3)

    S4 = '0123'
    expected_list_arr4 = [[]]
    test('test4', S4, expected_list_arr4)

    S5 = '1101111'
    expected_list_arr5 = [[110, 1, 111], [11, 0, 11, 11]]
    test('test5', S5, expected_list_arr5)


# Given a string S of digits, such as S = "123456579", 
# we can split it into a Fibonacci-like sequence [123, 456, 579].

# Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

# 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
# F.length >= 3;
# and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
# Also, note that when splitting the string into pieces, each piece must 
# not have extra leading zeroes, except if the piece is the number 0 itself.

# Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

# Example 1:

# Input: "123456579"
# Output: [123,456,579]

# Example 2:

# Input: "11235813"
# Output: [1,1,2,3,5,8,13]

# Example 3:

# Input: "112358130"
# Output: []
# Explanation: The task is impossible.

# Example 4:

# Input: "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.

# Example 5:

# Input: "1101111"
# Output: [110, 1, 111]
# Explanation: The output [11, 0, 11, 11] would also be accepted.
# Note:

# 1 <= S.length <= 200
# S contains only digits.
