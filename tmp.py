class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ']': '[',
            '}': '{',
            ')': '(',
        }
        stack = []
        for i, v in enumerate(s):
            if v in mapping.values():
                stack.append(v)
            if v in mapping.keys():
                if stack != [] and mapping[v] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack == []