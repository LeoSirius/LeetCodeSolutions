#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        vector<vector<int>> res;
        if (intervals.empty())
            return res;

        sort(intervals.begin(), intervals.end());
        res.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); ++i) {
            // 如果新区间的起点都在后面，（即没有交集）则直接push_back
            // 如果新区间和现有区间有交集，则现有区间最后取两者最大值
            if (intervals[i][0] <= res.back()[1])
                res.back()[1] = max(res.back()[1], intervals[i][1]);
            else
                res.push_back(intervals[i]);
        }
        return res;
    }
};

void test(string test_name, vector<vector<int>>& intervals, vector<vector<int>> &expected)
{
    vector<vector<int>> res = Solution().merge(intervals);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<vector<int>> intervals1 = {
        {1,3},
        {2,6},
        {8,10},
        {15,18}
    };
    vector<vector<int>> expected1 = {
        {1,6},
        {8,10},
        {15,18}
    };
    test("test1", intervals1, expected1);

    vector<vector<int>> intervals2 = {
        {1,4},
        {4,5}
    };
    vector<vector<int>> expected2 = {
        {1,5},
    };
    test("test2", intervals2, expected2);

    vector<vector<int>> intervals3 = {
        {1,4},
        {0,4}
    };
    vector<vector<int>> expected3 = {
        {0,4}
    };
    test("test3", intervals3, expected3);

    vector<vector<int>> intervals4 = {
        {1,4},
        {2,3}
    };
    vector<vector<int>> expected4 = {
        {1,4}
    };
    test("test4", intervals4, expected4);

    return 0;
}