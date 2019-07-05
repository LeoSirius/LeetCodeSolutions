## 思路1 从两边到中间宽度递减算water

`crystal clear`的solution [link](https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation)


```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size()-1;
        int max_water = 0;
        while(left < right){
            max_water = max(max_water, (right-left) * min(height[right], height[left]));
            if(height[left] < height[right]){
                left++;
            }else{
                right--;
            }
        }
        return max_water;
    }
};
```

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j-i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
```