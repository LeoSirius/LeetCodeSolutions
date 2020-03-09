from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for i in range(n)]
        cnt = 1
        j = 0

        while cnt <= n * n:
            # [j, n-j)  
            for i in range(j, n - j):
                res[j][i] = cnt
                cnt += 1

            # [j+1, n-j)   j的情况已经在上面加入了，即右上角
            for i in range(j + 1, n - j):
                res[i][n-j-1] = cnt    # 移动行，列贴在最右边。最右列和最右行都是n-j-1
                cnt += 1

            # [n-j-2, j-1) 本来应该从是n-j-1开始，即右下角，但是也已经加入了
            for i in range(n - j - 2, j - 1, -1):
                res[n-j-1][i] = cnt       # 移动列，行贴在最下面
                cnt += 1

            # [n-j-2, j)  左上角不用加，在下一轮新开始的时候加
            for i in range(n - j - 2, j, -1):
                res[i][j] = cnt
                cnt += 1
            
            j += 1

        return res


def test(test_name, n, expected):
    res = Solution().generateMatrix(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 3
    expected1 = [
        [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]
    ]
    test('test1', n1, expected1)


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        array = [[0 for i in range(n)] for j in range(n)]
        c, j = 1, 0
        while c<=n*n:
            # 从左向右
            for i in range(j, n-j):
                array[j][i] = c
                c += 1
            # 从上往下走
            for i in range(j+1, n-j):
                array[i][n-j-1] = c
                c += 1
            # 从右往左走
            for i in range(n-j-2, j-1, -1):
                array[n-j-1][i] = c
                c += 1
            # 从下往上走
            for i in range(n-j-2, j, -1):
                array[i][j] = c
                c += 1
            j += 1
        return array