from typing import *
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mp = defaultdict(int)   # key: str,  value: occurence
        for i in range(len(s)-9):
            mp[s[i:i+10]] += 1
        res = []
        for k, v in mp.items():
            if v >= 2:
                res.append(k)
        return res


def test(test_name, s, expected):
    res = Solution().findRepeatedDnaSequences(s)
    if sorted(res) == sorted(expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    expected1 = ["AAAAACCCCC", "CCCCCAAAAA"]
    test("test1", s1, expected1)


# All DNA is composed of a series of nucleotides abbreviated as A, C, G,
#  and T, for example: "ACGAATTCCG". When studying DNA, 
# it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings)
#  that occur more than once in a DNA molecule.

# Example:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
