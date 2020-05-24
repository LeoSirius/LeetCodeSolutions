#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total_remain = 0, run = 0, start = 0;
        for (int i = 0; i < gas.size(); i++) {
            run += gas[i] - cost[i];
            total_remain += gas[i] - cost[i];
            if (run < 0) {
                run = 0;
                start = i;
            }
        }
        return 0 <= total_remain ? start : -1;
    }
};


void test(string test_name, vector<int>& gas, vector<int>& cost, int expected)
{
    int res = Solution().canCompleteCircuit(gas, cost);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}


int main()
{
    vector<int> gas1 = {1,2,3,4,5};
    vector<int> cost1 = {3,4,5,1,2};
    int expected1 = 3;
    test("test1", gas1, cost1, expected1);

    vector<int> gas2 = {2,3,4};
    vector<int> cost2 = {3,4,3};
    int expected2 = -1;
    test("test2", gas2, cost2, expected2);

    return 0;
}
