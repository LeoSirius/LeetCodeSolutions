#include <iostream>
using namespace std;

class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int left = max(A, E);
        int right = max(min(C, G), left);  // if not overlapped, this ensure right-left=0
        int bottom = max(B, F);
        int top = max(min(D, H), bottom);

        // 先减后加防止溢出
        return (C-A)*(D-B) - (right-left)*(top-bottom) + (G-E)*(H-F);
    }
};

void test(string test_name, int A, int B, int C, int D, int E, int F, int G, int H, int expected)
{
    Solution s;
    int res = s.computeArea(A,B,C,D,E,F,G,H);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int A1 = -3, B1 = 0, C1 = 3, D1 = 4, E1 = 0, F1 = -1, G1 = 9, H1 = 2;
    int expected1 = 45;
    test("test1", A1,B1,C1,D1,E1,F1,G1,H1, expected1);

    int A2 = 0, B2 = 0, C2 = 50000, D2 = 40000, E2 = 0, F2 = 0, G2 = 50000, H2 = 40000;
    int expected2 = 2000000000;
    test("test2", A2, B2, C2, D2, E2, F2, G2, H2, expected2);

    return 0;
}
