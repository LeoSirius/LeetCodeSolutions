from typing import *

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        pass


def test(test_name, s, expected):
    res = Solution().findRepeatedDnaSequencess(s)
    if sorted(res) == sorted(expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    expected = ["AAAAACCCCC", "CCCCCAAAAA"]


# All DNA is composed of a series of nucleotides abbreviated as A, C, G,
#  and T, for example: "ACGAATTCCG". When studying DNA, 
# it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings)
#  that occur more than once in a DNA molecule.

# Example:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

# Output: ["AAAAACCCCC", "CCCCCAAAAA"]

