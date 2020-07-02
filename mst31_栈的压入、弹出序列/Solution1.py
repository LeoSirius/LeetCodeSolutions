from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        p1, p2 = 0, 0
        while p1 < len(pushed):
            stk.append(pushed[p1])
            p1 += 1
            while stk and stk[-1] == popped[p2]:
                stk.pop()
                p2 += 1
        return p2 == len(popped)

def test(test_name, pushed: List[int], popped: List[int], expected):
    res = Solution().validateStackSequences(pushed, popped)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    pushed1 = [1,2,3,4,5]
    popped1 = [4,5,3,2,1]
    expected1 = True
    test('test1', pushed1, popped1, expected1)

    pushed2 = [1,2,3,4,5]
    popped2 = [4,3,5,1,2]
    expected2 = False
    test('test2', pushed2, popped2, expected2)

# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1}
# 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。
#
#  
#
# 示例 1：
#
# 输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# 输出：true
# 解释：我们可以按以下顺序执行：
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#
#
#
# 示例 2：
# 输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# 输出：false
# 解释：1 不能在 2 之前弹出。
#  
#
# 提示：
#
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed 是 popped 的排列。
