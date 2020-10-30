### 思路1

方法一： 集合 Set + 遍历
遍历五张牌，遇到大小王（即 00 ）直接跳过。
判别重复： 利用 Set 实现遍历判重， Set 的查找方法的时间复杂度为 O(1)O(1) ；
获取最大 / 最小的牌： 借助辅助变量 max 和 min ，遍历统计即可。最大牌 - 最小牌 < 5 则可构成顺子

<!-- 
class Solution {
    public boolean isStraight(int[] nums) {
        Set<Integer> repeat = new HashSet<>();
        int max = 0, min = 14;
        for(int num : nums) {
            if(num == 0) continue; // 跳过大小王
            max = Math.max(max, num); // 最大牌
            min = Math.min(min, num); // 最小牌
            if(repeat.contains(num)) return false; // 若有重复，提前返回 false
            repeat.add(num); // 添加此牌至 Set
        }
        return max - min < 5; // 
    }
} -->


