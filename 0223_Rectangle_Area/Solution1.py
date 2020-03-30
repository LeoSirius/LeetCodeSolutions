class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        left = max(A, E)
        right = max(left, min(C, G))
        bottom = max(B, F)
        top = max(min(D, H), bottom)

        return (C - A) * (D - B) - (right - left) * (top - bottom) + (G - E) * (H - F)


def test(test_name, A, B, C, D, E, F, G, H, expected):
    res = Solution().computeArea(A, B, C, D, E, F, G, H)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    A1, B1, C1, D1, E1, F1, G1, H1 = -3, 0, 3, 4, 0, -1, 9, 2
    expected1 = 45
    test('test1', A1, B1, C1, D1, E1, F1, G1, H1, expected1)

    A2, B2, C2, D2, E2, F2, G2, H2 = 0, 0, 50000, 40000, 0, 0, 50000, 40000
    expected2 = 2000000000
    test('test2', A2, B2, C2, D2, E2, F2, G2, H2, expected2)
