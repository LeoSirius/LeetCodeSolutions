#include <iostream>
#include <vector>
using namespace std;

class Solution {
    bool static cmp(vector<int> a, vector<int> b)
    {
        return a[1] < b[1];
    }
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size() == 0)
            return 0;
        sort(points.begin(), points.end(), cmp);
        int shots = 1;
        int shot_at = points[0][1];
        for (int i = 0; i < points.size(); i++) {
            if (shot_at < points[i][0]) {
                shot_at = points[i][1];
                shots++;
            }
        }
        return shots;
    }
};

void test(string test_name, vector<vector<int>>& points, int expected)
{
    int res = Solution().findMinArrowShots(points);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<vector<int>> points1 = {
        {10, 16}, {2, 8}, {1, 6}, {7, 12}
    };
    int expected1 = 2;
    test("test1", points1, expected1);

    return 0;
}

// There are a number of spherical balloons spread in two-dimensional space. 
// For each balloon, provided input is the start and end coordinates of 
// the horizontal diameter. Since it's horizontal, y-coordinates don't 
// matter and hence the x-coordinates of start and end of the diameter suffice.
//  Start is always smaller than end. There will be at most 104 balloons.

// An arrow can be shot up exactly vertically from different points along 
// the x-axis. A balloon with xstart and xend bursts by an arrow shot at x 
// if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can 
// be shot. An arrow once shot keeps travelling up infinitely.
//  The problem is to find the minimum number of arrows that must be shot to 
// burst all balloons.

// Example:

// Input:
// [[10,16], [2,8], [1,6], [7,12]]

// Output:
// 2

// Explanation:
// One way is to shoot one arrow for example at x = 6
//  (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11
//  (bursting the other two balloons).
