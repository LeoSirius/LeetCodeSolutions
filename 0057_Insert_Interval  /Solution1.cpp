#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;
        int i = 0;

        // 当前指向区间的结尾 小于 新区间的开头，直接放入res
        while (i < intervals.size() && intervals[i][1] < newInterval[0])
            res.push_back(intervals[i++]);

        // 当前指向区间的开头 小于等于 新区间的结尾，即在overlapping中，不断更新新区间
        while (i < intervals.size() && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            ++i;
        }
        res.push_back(newInterval);

        while (i < intervals.size())
            res.push_back(intervals[i++]);

        return res;
    }
};

void test(string test_name, vector<vector<int>>& intervals, vector<int>& newInterval, vector<vector<int>>& expected)
{
    vector<vector<int>> res = Solution().insert(intervals, newInterval);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<vector<int>> intervals1 = {{1,3}, {6,9}};
    vector<int> newInterval1 = {2,5};
    vector<vector<int>> expected1 = {{1,5}, {6,9}};
    test("test1", intervals1, newInterval1, expected1);

    vector<vector<int>> intervals2 = {{1,2}, {3,5}, {6,7}, {8,10}, {12,16}};
    vector<int> newInterval2 = {4,8};
    vector<vector<int>> expected2 = {{1,2}, {3,10}, {12,16}};
    test("test2", intervals2, newInterval2, expected2);
    return 0;
}
