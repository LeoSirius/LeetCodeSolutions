from typing import *
from collections import defaultdict

class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        res = [0,0]
        smap, gmap = defaultdict(int), defaultdict(int)

        for i in range(4):
            smap[solution[i]] += 1
            gmap[guess[i]] += 1

        for i in range(4):
            if solution[i] == guess[i]:
                res[0] += 1
                smap[solution[i]] -= 1
                gmap[solution[i]] -= 1

        for k in gmap:
            if k in smap:
                res[1] += min(gmap[k], smap[k])

        return res


def test(test_name, solution, guess, expected):
    res = Solution().masterMind(solution, guess)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    solution1 = "RGBY"
    guess1 = "GGRR"
    expected1 = [1,1]
    test('test1', solution1, guess1, expected1)


# The Game of Master Mind is played as follows:

# The computer has four slots, and each slot will contain a ball that is 
# red (R). yellow (Y). green (G) or blue (B). For example, 
# the computer might have RGGB (Slot #1 is red, Slots #2 and 
# #3 are green, Slot #4 is blue).

# You, the user, are trying to guess the solution. You might,
#  for example, guess YRGB.

# When you guess the correct color for the correct slot, you
#  get a "hit:' If you guess a color that exists but is in the wrong slot, 
#  you get a "pseudo-hit:' Note that a slot that is a hit can never 
#  count as a pseudo-hit.

# For example, if the actual solution is RGBY and you guess GGRR, 
# you have one hit and one pseudo-hit. Write a method that, given a
#  guess and a solution, returns the number of hits and pseudo-hits.

# Given a sequence of colors solution, and a guess, write a method 
# that return the number of hits and pseudo-hit answer, where answer[0] 
# is the number of hits and answer[1] is the number of pseudo-hit.

# Example:

# Input:  solution="RGBY",guess="GGRR"
# Output:  [1,1]
# Explanation:  hit once, pseudo-hit once.
# Note:

# len(solution) = len(guess) = 4
# There are only "R","G","B","Y" in solution and guess.

