### 思路1 矩阵二分查找

判断mid在排序中的位置是否 >= k
如果 >= k说明k在mid前面（包括），right=mid
如果 <k 说明k在mid后面，left=mid+1