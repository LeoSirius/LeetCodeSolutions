from typing import *

class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        pa, pb = m - 1, n - 1
        tail = m + n - 1

        while pa >= 0 and pb >= 0:
            if A[pa] > B[pb]:
                A[tail] = A[pa]
                pa -= 1
            else:
                A[tail] = B[pb]
                pb -= 1
            tail -= 1

        # 我们以A为基准，这个不用判断，若pb = -1, 则tail 必然等于pa
        # while pa >= 0:
        #     A[tail] = A[pa]
        #     tail -= 1
        #     pa -= 1

        while pb >= 0:
            A[tail] = B[pb]
            tail -= 1
            pb -= 1


def test(test_name, A, m, B, n, expected):
    Solution().merge(A, m, B, n)
    if A == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    A1 = [1,2,3,0,0,0]
    m1 = 3
    B1 = [2,5,6]
    n1 = 3
    expected1 = [1,2,2,3,5,6]
    test('test1', A1, m1, B1, n1, expected1)


# You are given two sorted arrays, A and B, where A has a 
# large enough buffer at the end to hold B. Write a method to 
# merge B into A in sorted order.

# Initially the number of elements in A and B are m and n respectively.

# Example:

# Input:
# A = [1,2,3,0,0,0], m = 3
# B = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]

