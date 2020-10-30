#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0)
            return 0;
        int K = 2;
        vector<vector<int>> dp(K + 1, vector<int>(prices.size(), 0));
        for (int k = 1; k <= 2; ++k) {
            int cur_min = prices[0];
            // 把思路中的j压缩到了cur_min，减少了一重循环，否则会超时
            for (int i = 1; i < prices.size(); ++i) {
                cur_min = min(cur_min, (prices[i] - dp[k-1][i-1]));
                dp[k][i] = max(dp[k][i-1], prices[i] - cur_min);
            }
        }
        return dp.back().back();
    }
};

void test(string test_name, vector<int>& prices, int expected)
{
    int res = Solution().maxProfit(prices);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> prices1 = {3,3,5,0,0,3,1,4};
    int expected1 = 6;
    test("test1", prices1, expected1);

    vector<int> prices2 = {1,2,3,4,5};
    int expected2 = 4;
    test("test2", prices2, expected2);

    vector<int> prices3 = {7,6,4,3,1};
    int expected3 = 0;
    test("test3", prices3, expected3);

    return 0;
}
