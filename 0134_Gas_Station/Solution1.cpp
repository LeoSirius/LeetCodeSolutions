#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total_remain = 0, run = 0, start = 0;
        for (int i = 0; i < gas.size(); i++) {
            run += (gas[i] - cost[i]);
            total_remain += (gas[i] - cost[i]);
            // total_remain表示总加油和总耗油之差，如果这个数小于0，则必然完不成绕圈。
            // 为什么如果k+1->end全部可以正常通行，且total_remain>=0就可以说明车子从k+1站点出发可以开完全程？
            // 因为，起始点将当前路径分为A、B两部分。其中，必然有(1)A部分剩余油量<0。(2)B部分剩余油量>0。
            // 所以，无论多少个站，都可以抽象为两个站点（A、B）。(1)从B站加满油出发，(2)开往A站，车加油，(3)再开回B站的过程。
            // B剩余的油>=A缺少的总油（因为total_remain>=0）。必然可以推出，B剩余的油>=A站点的每个子站点缺少的油。

            // run表示当前剩下的油量，如果小于0，则起点重新计算。
            if (run < 0) {
                start = i + 1;
                run = 0;
            }
        }
        return total_remain >= 0 ? start : -1;
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
