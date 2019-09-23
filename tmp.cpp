class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int new_tail = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (val != nums[i]) {
                nums[++new_tail] = nums[i];
            }
        }
        return new_tail+1;
    }
};