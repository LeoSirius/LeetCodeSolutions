from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n, m = len(ring), len(key)
        pos = defaultdict(list)

        for idx, ch in enumerate(ring):
            pos[ch].append(idx)

        
        dp = [[float('inf')] * n for _ in range(m)]

        # 对key的第一个字符，把pos里面x到key中x的距离初始化好
        for idx in pos[key[0]]:
            dp[0][idx] = min(idx, n - idx) + 1

        for i in range(1, m):
            for j in pos[key[i]]:
                for k in pos[key[i]]:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + min(abs(j-k), n-abs(j-k)) + 1)

        return min(dp[-1])


def test(test_name, ring, key, expected):
    res = Solution().findRotateSteps(ring, key)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    ring1 = "godding"
    key1 = "gd"
    expected1 = 4
    test('test1', ring1, key1, expected1)


# In the video game Fallout 4, the quest "Road to Freedom" requires players 
# to reach a metal dial called the "Freedom Trail Ring", and use the dial 
# to spell a specific keyword in order to open the door.

# Given a string ring, which represents the code engraved on the outer 
# ring and another string key, which represents the keyword needs to be spelled.
#  You need to find the minimum number of steps in order to spell all the
#  characters in the keyword.

# Initially, the first character of the ring is aligned at 12:00 direction. 
# You need to spell all the characters in the string key one by one by rotating
# the ring clockwise or anticlockwise to make each character of the 
# string key aligned at 12:00 direction and then by pressing the center button.

# At the stage of rotating the ring to spell the key character key[i]:

# You can rotate the ring clockwise or anticlockwise one place,
#  which counts as 1 step. The final purpose of the rotation is to align 
# one of the string ring's characters at the 12:00 direction, 
# where this character must equal to the character key[i].

# If the character key[i] has been aligned at the 12:00 direction, 
# you need to press the center button to spell, which also counts as 1 step.
#  After the pressing, you could begin to spell the next character in the key 
# (next stage), otherwise, you've finished all the spelling.


# Input: ring = "godding", key = "gd"
# Output: 4
# Explanation:
# For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
# For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
# Also, we need 1 more step for spelling.
# So the final output is 4.
# Note:

# Length of both ring and key will be in range 1 to 100.
# There are only lowercase letters in both strings and might be some duplcate characters in both strings.
# It's guaranteed that string key could always be spelled by rotating the string ring.

