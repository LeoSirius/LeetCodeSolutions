#include <iostream>
#include <vector>
using namespace std;

class Solution {
    bool static compare(vector<int> a, vector<int> b)
    {
        return a[1] < b[1];
    }
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.size() <= 1)
            return 0;
        sort(intervals.begin(), intervals.end(), compare);
        int num_not_lapped = 1;
        int last_end = intervals[0][1];
        for (int i = 1; i < intervals.size(); i++) {
            if (last_end <= intervals[i][0]) {
                num_not_lapped++;
                last_end = intervals[i][1];
            }
        }
        return intervals.size() - num_not_lapped;
    }
};

void test(string test_name, vector<vector<int>>& intervals, int expected)
{
    int res = Solution().eraseOverlapIntervals(intervals);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<vector<int>> intervals1 = {
        {1,2}, {2,3}, {3,4}, {1,3}
    };
    int expected1 = 1;
    test("test1", intervals1, expected1);

    vector<vector<int>> intervals2 = {
        {1,2}, {1,2}, {1,2}
    };
    int expected2 = 2;
    test("test2", intervals2, expected2);

    vector<vector<int>> intervals3 = {
        {1,2}, {2,3}
    };
    int expected3 = 0;
    test("test3", intervals3, expected3);

    vector<vector<int>> intervals4 = {};
    int expected4 = 0;
    test("test4", intervals4, expected4);

    return 0;
}

// Given a collection of intervals, find the minimum number of 
// intervals you need to remove to make the rest of the intervals
//  non-overlapping.

// Example 1:
// Input: [[1,2],[2,3],[3,4],[1,3]]
// Output: 1
// Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

// Example 2:
// Input: [[1,2],[1,2],[1,2]]
// Output: 2
// Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

// Example 3:
// Input: [[1,2],[2,3]]
// Output: 0
// Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

// Note:

// You may assume the interval's end point is always bigger than its start point.
// Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.


