#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.size() == 0)
            return 0;
        // vector排序可以直接用sort，类似string的比较。
        // vector会找到第一个不同的元素最为排序的依据。这正好是我们需要的。
        // 如果第一个元素相同，会使用第二个元素
        sort(intervals.begin(), intervals.end());
        priority_queue<int, vector<int>, greater<int>> hp;
        hp.push(intervals[0][1]);
        for (int i = 1; i < intervals.size(); i++) {
            if (hp.top() <= intervals[i][0])
                hp.pop();
            hp.push(intervals[i][1]);
        }

        return hp.size();
    }
};

void test(string test_name, vector<vector<int>>& intervals, int expected)
{
    int res = Solution().minMeetingRooms(intervals);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;

}

int main()
{
    vector<vector<int>> intervals1 = {
        {0, 30}, {5, 10}, {15, 20}
    };
    int expected1 = 2;
    test("test1", intervals1, expected1);

    vector<vector<int>> intervals2 = {
        {7, 10}, {2, 4}
    };
    int expected2 = 1;
    test("test2", intervals2, expected2);

    return 0;
}

// Given an array of meeting time intervals consisting of start and 
// end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of 
// conference rooms required.

// Example 1:

// Input: [[0, 30],[5, 10],[15, 20]]
// Output: 2
// Example 2:

// Input: [[7,10],[2,4]]
// Output: 1
