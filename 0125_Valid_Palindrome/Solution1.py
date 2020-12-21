class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = [ch for ch in s if ch.isalnum()]
        left, right = 0, len(l)-1
        while left < right:
            if l[left] != l[right]:
                break
            left += 1
            right -= 1
        return left >= right

def test(test_name, s, expected):
    res = Solution().isPalindrome(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    s1 = "A man, a plan, a canal: Panama";
    expected1 = True;
    test("test1", s1, expected1);

    s2 = "race a car";
    expected2 = False;
    test("test2", s2, expected2);
