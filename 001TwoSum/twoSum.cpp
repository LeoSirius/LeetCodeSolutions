class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		unordered_map<int, int> hash;
		vector<int> result;
		int i;
		for (i = 0; i < nums.size(); i++) {
			int numberToFind = target - nums[i];
			if (hash.find(numberToFind) != hash.end()) {
				result.push_back(hash[numberToFind]);
				result.push_back(i);
			}
			hash[nums[i]] = i;
		}
		return result;
	}
};