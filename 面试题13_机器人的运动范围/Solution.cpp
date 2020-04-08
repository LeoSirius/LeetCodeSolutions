#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
    int get_digit_sum(int m, int n)
    {
        int res = 0;
        while (m) {
            int tmp = m % 10;
            res += tmp;
            m /= 10;
        }
        while (n) {
            int tmp = n % 10;
            res += tmp;
            n /= 10;
        }
        return res;
    }
public:
    int movingCount(int m, int n, int k) {
        if (k == 0)
            return 1;
        vector<vector<int>> map(m, vector<int>(n, 0));
        map[0][0] = 1;
        queue<pair<int, int>> Q;
        Q.push({0, 0});
        int res = 1;

        // 分别向下和向右走
        int dx[2] = {0, 1};
        int dy[2] = {1, 0};

        while (!Q.empty()) {
            auto [x, y] = Q.front(); Q.pop();
            for (int i = 0; i < 2; ++i) {
                int tx = x + dx[i];
                int ty = y + dy[i];
                if (tx < 0 || tx >= m || ty < 0 || ty >= n || map[tx][ty] || get_digit_sum(tx, ty) > k)
                    continue;
                Q.push({tx, ty});
                map[tx][ty] = 1;
                ++res;
            }
        }
        return res;
    }
};

void test(string test_name, int m, int n, int k, int expected)
{
    int res = Solution().movingCount(m, n, k);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int m1 = 2, n1 = 3, k1 = 1;
    int expected1 = 3;
    test("test1", m1, n1, k1, expected1);

    int m2 = 3, n2 = 1, k2 = 0;
    int expected2 = 1;
    test("test2", m2, n2, k2, expected2);

    return 0;
}
