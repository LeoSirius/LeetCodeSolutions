### 思路1 前缀和

设index左边的和为left_sum，满足条件的idx会有下面的等式成立


left_sum == total - nums[idx] - left_sum

total - nums[idx] - left_sum 就是 right_sum
