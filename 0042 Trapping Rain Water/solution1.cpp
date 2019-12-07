#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int l, r, max_l, max_r, res;
        l = 0, r = height.size() - 1;
        max_l = max_r = 0;
        res = 0;

        while (l <= r) {
            if (height[l] < height[r]) {
                if (max_l <= height[l]) max_l = height[l];
                else res += max_l - height[l];
                l++;
            } else {
                if (max_r <= height[r]) max_r = height[r];
                else res += max_r - height[r];
                r--;
            }
        }
        return res;
    }
};

int main()
{
    return 0;
}