#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        int size = costs.size();
        if (size < 1) return 0;
        vector<vector<int>> dp(costs.size(), vector<int>(costs[0].size(), 0));
        for (int i = 0; i < 3; i++) {
            dp[0][i] = costs[0][i];
        }
        for (int i = 1; i < costs.size(); i++) {
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0];
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1];
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2];
        }
        return min(min(dp[size-1][0], dp[size-1][1]), dp[size-1][2]);
    }
};

void test(string test_name, vector<vector<int>> &costs, int expected)
{
    if (Solution().minCost(costs) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<vector<int>> costs1 = {
        {17, 2, 17},{16,16,5},{14,3,19}
    };
    int expected1 = 10;
    test("test1", costs1, expected1);


    vector<vector<int>> costs2 = {};
    int expected2 = 0;
    test("test2", costs2, expected2);

    return 0;
}
