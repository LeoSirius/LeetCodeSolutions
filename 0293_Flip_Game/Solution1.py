from typing import *

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        res = []
        _len = len(currentState)
        if _len < 2:
            return res

        for i in range(1, _len):
            if currentState[i] == currentState[i-1] == '+':
                state = currentState[:i-1] + '--' + currentState[i+1:]
                res.append(state)
        return res


def test(test_name, currentState, expected):
    res = Solution().generatePossibleNextMoves(currentState)
    res.sort()
    expected.sort()
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    currentState1 = "++++"
    expected1 = ["--++","+--+","++--"]
    test('test1', currentState1, expected1)

    currentState2 = '+'
    expected2 = []
    test('test2', currentState2, expected2)
