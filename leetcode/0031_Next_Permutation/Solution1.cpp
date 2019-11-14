#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len = nums.size();
        if (len == 0) return;
        int idx_left, idx_right;
        for (idx_left = len - 2; idx_left >= 0; idx_left--) {
            if (nums[idx_left] < nums[idx_left+1]) {
                break;                 // e.g. [1 2 3 9 8 7], k = 2, point to 3
            }
        }
        if (idx_left == -1) {
            reverse(nums.begin(), nums.end());    // e.g. [3,2,1] to [1,2,3]
            return;
        }
        for (int idx_right = len - 1; idx_right > idx_left; idx_right--) {
            if (nums[idx_right] > nums[idx_left]) {
                swap(nums[idx_left], nums[idx_right]);     // let l point the first larger than nums[k]'s number counting from back
                break;
            }
        }
        reverse(nums.begin() + idx_left + 1, nums.end());
    }
};

int main()
{

}