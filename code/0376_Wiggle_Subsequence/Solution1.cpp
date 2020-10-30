#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if (nums.size() < 2)
            return nums.size();
        
        int up = 1, down = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i-1] < nums[i])
                up = down + 1;
            else if (nums[i] < nums[i-1])
                down = up + 1;
        }
        return max(up, down);
    }
};

void test(string test_name, vector<int> nums, int expected)
{
    int res = Solution().wiggleMaxLength(nums);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {1,7,4,9,2,5};
    int expected1 = 6;
    test("test1", nums1, expected1);

    vector<int> nums2 = {1,17,5,10,13,15,10,5,16,8};
    int expected2 = 7;
    test("test2", nums2, expected2);

    vector<int> nums3 = {1,2,3,4,5,6,7,8,9};
    int expected3 = 2;
    test("test3", nums3, expected3);

    vector<int> nums4 = {0,0};
    int expected4 = 1;
    test("test4", nums4, expected4);

    return 0;
}

// A sequence of numbers is called a wiggle sequence if the 
// differences between successive numbers strictly alternate 
// between positive and negative. The first difference (if one exists)
//  may be either positive or negative. A sequence with fewer than two elements 
// is trivially a wiggle sequence.

// For example, [1,7,4,9,2,5] is a wiggle sequence because the differences 
// (6,-3,5,-7,3) are alternately positive and negative. In contrast, 
// [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, 
// the first because its first two differences are positive and the second 
// because its last difference is zero.

// Given a sequence of integers, return the length of the longest 
// subsequence that is a wiggle sequence. A subsequence is obtained 
// by deleting some number of elements (eventually, also zero) from the 
// original sequence, leaving the remaining elements in their original order.

// Example 1:
// Input: [1,7,4,9,2,5]
// Output: 6
// Explanation: The entire sequence is a wiggle sequence.

// Example 2:
// Input: [1,17,5,10,13,15,10,5,16,8]
// Output: 7
// Explanation: There are several subsequences that achieve this
//  length. One is [1,17,10,13,10,16,8].

// Example 3:
// Input: [1,2,3,4,5,6,7,8,9]
// Output: 2

// Follow up:
// Can you do it in O(n) time?

