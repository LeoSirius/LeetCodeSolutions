#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res = {-1, -1};
        if (nums.size() == 0) return res;

        int left = 0, right = nums.size() - 1;
        int mid;
        while (left < right) {
            mid = left + (right - left) / 2;
            if (target > nums[mid]) left = mid + 1;
            else right = mid;
        }
        if (nums[left] != target) return res;       // target不在nums中
        else res[0] = left;

        right = nums.size() - 1;                    // left不用重置
        while (left < right) {
            mid = left + (right - left) / 2 + 1;    // +1 make mid biased to right
            if (target < nums[mid]) right = mid - 1;
            else left = mid;
        }
        res[1] = right;
        return res;
    }
};

int main()
{
    return 0;
}
