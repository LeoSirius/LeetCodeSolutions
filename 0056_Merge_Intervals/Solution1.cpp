#include<iostream>
#include<vector>
using namespace std;

class Solution {
    static bool compare_first_element(vector<int> a, vector<int> b)
    {
        return a[0] < b[0];
    }
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        if (intervals.empty()) return res;
        sort(intervals.begin(), intervals.end(), compare_first_element);
        res.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); i++) {
            if (res.back()[1] < intervals[i][0]) {
                res.push_back(intervals[i]);
            } else {
                res.back()[1] = max(res.back()[1], intervals[i][1]);
            }
        }
        return res;
    }
};

void test(string test_name, vector<vector<int>> &intervals, vector<vector<int>> &expected)
{
    Solution s;
    if (s.merge(intervals) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
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

    return 0;
}
