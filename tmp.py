class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '{': stack.append('}')
            elif c == '[': stack.append(']')
            elif c == '(': stack.append(')')
            else:
                if stack == [] or c != stack.pop():
                    return False
        return stack == []