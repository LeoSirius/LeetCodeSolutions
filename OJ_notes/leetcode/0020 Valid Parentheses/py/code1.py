class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mydict = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in mydict.values():
                stack.append(char)
            elif char in mydict.keys():
                if stack == [] or mydict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
