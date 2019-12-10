#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int total = 0;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] > prices[i-1])
                total += prices[i] - prices[i-1];
        }
        return total;
    }
};

void test(string test_name, vector<int>& prices, int expected)
{
    Solution s;
    if (s.maxProfit(prices) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> prices1 = {7,1,5,3,6,4};
    int expected1 = 7;
    test("test1", prices1, expected1);

    vector<int> prices2 = {1,2,3,4,5};
    int expected2 = 4;
    test("test2", prices2, expected2);

    vector<int> prices3 = {7,6,4,3,1};
    int expected3 = 0;
    test("test3", prices3, expected3);

    return 0;
}

// Input: [7,1,5,3,6,4]
// Output: 7
// Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
//              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
// Example 2:

// Input: [1,2,3,4,5]
// Output: 4
// Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
//              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
//              engaging multiple transactions at the same time. You must sell before buying again.
// Example 3:

// Input: [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transaction is done, i.e. max profit = 0.
