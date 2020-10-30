#include <iostream>
#include <vector>
using namespace std;

class Solution {
    bool static cmp(vector<int> a, vector<int> b)
    {
        if (a[0] == b[0])
            return a[1] < b[1];
        return a[0] > b[0];
    }
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), cmp);
        vector<vector<int>> res;
        for (int i = 0; i < people.size(); i++) {
            res.insert(res.begin()+people[i][1], {people[i][0], people[i][1]});
        }
        return res;
    }
};

void test(string test_name, vector<vector<int>>& people, vector<vector<int>> expected)
{
    vector<vector<int>> res = Solution().reconstructQueue(people);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<vector<int>> people1 = {
        {7,0}, {4,4}, {7,1}, {5,0}, {6,1}, {5,2}
    };
    vector<vector<int>> expected1 = {
        {5,0}, {7,0}, {5,2}, {6,1}, {4,4}, {7,1}
    };
    test("test1", people1, expected1);

    return 0;
}


// Suppose you have a random list of people standing in a queue.
// Each person is described by a pair of integers (h, k), 
// where h is the height of the person and k is the number of people in front of 
// this person who have a height greater than or equal to h. Write an algorithm 
// to reconstruct the queue.

// Note:
// The number of people is less than 1,100.

//  
// Example

// Input:
// [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

// Output:
// [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

