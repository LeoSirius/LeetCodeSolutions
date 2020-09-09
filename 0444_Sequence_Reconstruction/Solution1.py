from typing import *

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:

        if not seqs:
            return False
        # 测试用例有这个输入，需要检查
        if all(seq == [] for seq in seqs):
            return False

        size = len(org)
        # 这道题org是从1开始的，多申请一个空间，方便所有都从1开始
        indegrees, successors = [0 for _ in range(size+1)], [set() for _ in range(size+1)]

        for seq in seqs:
            if any(s < 1 or size < s for s in seq):
                return False
            for i in range(1, len(seq)):
                if seq[i] not in successors[seq[i-1]]:
                    indegrees[seq[i]] += 1
                    successors[seq[i-1]].add(seq[i])

        layer = [i for i in org if not indegrees[i]] # 先把入度为0的结点取出来放到layer中
        for x in range(size):
            if len(layer) != 1 or layer[0] != org[x]:
                return False

            next_layer = []
            for successor in successors[layer[0]]:
                indegrees[successor] -= 1
                if not indegrees[successor]:
                    next_layer.append(successor)
            layer = next_layer
        return True


def test(test_name, org, seqs, expected):
    res = Solution().sequenceReconstruction(org, seqs)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    org1 = [1,2,3]
    seqs1 = [[1,2],[1,3]]
    expected1 = False
    test('test1', org1, seqs1, expected1)

    org2 = [1,2,3]
    seqs2 = [[1,2]]
    expected2 = False
    test('test2', org2, seqs2, expected2)

    org3 = [1,2,3]
    seqs3 = [[1,2],[1,3],[2,3]]
    expected3 = True
    test('test3', org3, seqs3, expected3)

    org4 = [4,1,5,2,6,3]
    seqs4 = [[5,2,6,3],[4,1,5,2]]
    expected4 = True
    test('test4', org4, seqs4, expected4)

    org5 = [1]
    seqs5 = [[],[]]
    expexted5 = False
    test('test5', org5, seqs5, expexted5)

    org6 = [3,7,6,4,8,2,10,1,5,9]
    seqs6 = [[7,6,4,8,2,10,1,5,9],[4,8,2,10,1,5],[2,10,1,5],[10,1,5,9],[1,5,9],[8,2,10,1,5,9],[9],[],[6,4],[3,7,6,4,8,2,10,1]]
    expected6 = True
    test('test6', org6, seqs6, expected6)


# Check whether the original sequence org can be uniquely reconstructed from 
# the sequences in seqs. 
# The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104.
#  Reconstruction means building a shortest common supersequence of the
#   sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are
#    subsequences of it). Determine whether there is only one sequence that can be 
#    reconstructed from seqs and it is the org sequence.

# Example 1:
# Input: org = [1,2,3], seqs = [[1,2],[1,3]]
# Output: false
# Explanation: [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

# Example 2:
# Input: org = [1,2,3], seqs = [[1,2]]
# Output: false
# Explanation: The reconstructed sequence can only be [1,2].

# Example 3:
# Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
# Output: true
# Explanation: The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

# Example 4:
# Input: org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
# Output: true

# Constraints:
# 1 <= n <= 10^4
# org is a permutation of {1,2,...,n}.
# seqs[i][j] fits in a 32-bit signed integer.
