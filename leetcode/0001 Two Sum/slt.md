## 思路1 利用hash的思想

由于最后要返回的是索引的数组。用hash的key来存放数组中一个元素的值，而用hash的value来存放那个值得索引。这样就建立了数组元素值对数组元素索引的映射。

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // key is value in nums, value of hash is its indx
        unordered_map<int, int> hash;
        vector<int> result;
        for(int i = 0; i < nums.size(); i++){
            int num_to_find = target - nums[i];

            if(hash.find(num_to_find) != hash.end()){
                result.push_back(hash[num_to_find]);
                result.push_back(i);
                break;   // exactly one solution
            }else{
                hash[nums[i]] = i;
            }
        }
        return result;
    }
};
```

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: nums' element, value: index of that element
        mapping = {}
        for i in range(len(nums)):
            num_to_find = target - nums[i]
            if num_to_find in mapping.keys():
                return [i, mapping[num_to_find]]
            else:
                mapping[nums[i]] = i
```