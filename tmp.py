class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            max_water = max(max_water, (right-left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_water