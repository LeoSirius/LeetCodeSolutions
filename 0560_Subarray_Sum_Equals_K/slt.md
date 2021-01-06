### 思路1 前缀和 + hash

一次遍历搞定

preSum[i]定义为 nums[0] + nums[1] + ... + nums[i]

那么preSum[i] - preSum[j-1]就是   nums[j] + nums[j+1] + ... + nums[i-1] + nums[i]

如果[j, i]区间的和是k，那么就有preSum[i] - preSum[j-1] == k

-> preSum[i] - k == preSum[j-1]


