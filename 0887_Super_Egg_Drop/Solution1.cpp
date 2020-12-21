#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int superEggDrop(int K, int N) {
        vector<vector<int>> dp(N + 1, vector<int>(K + 1, 0));
        int f = 0;

        // 操作次数要最小，所以f从1开始，慢慢增加
        // 情况要最坏，所以是本楼层1 + 本楼层下面能确定的楼层数量 + 本楼层上面能确定的数量
        while (dp[f][K] < N) {
            f++;
            for (int k = 1; k <= K; ++k)
                dp[f][k] = dp[f-1][k] + dp[f-1][k-1] + 1;
        }
        return f;
    }
};

void test(string test_name, int K, int N, int expected)
{
    int res = Solution().superEggDrop(K, N);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int K1 = 1, N1 = 2;
    int expected1 = 2;
    test("test1", K1, N1, expected1);

    int K2 = 2, N2 = 6;
    int expected2 = 3;
    test("test2", K2, N2, expected2);

    int K3 = 3, N3 = 14;
    int expected3 = 4;
    test("test3", K3, N3, expected3);

    return 0;
}
