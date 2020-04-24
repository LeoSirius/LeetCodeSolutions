from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        for lena in range(1, 4):
            for lenb in range(1, 4):
                for lenc in range(1, 4):
                    for lend in range(1, 4):
                        if lena + lenb + lenc + lend == len(s):
                            a = int(s[:lena])
                            if a > 255: continue
                            b = int(s[lena:lena + lenb])
                            if b > 255: continue
                            c = int(s[lena+lenb:lena+lenb+lenc])
                            if c > 255: continue
                            d = int(s[lena+lenb+lenc:])
                            if d > 255: continue
                            new_str = str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)
                            if len(new_str) == len(s) + 3:
                                res.append(new_str)
        return res

def test(test_name, s, expected):
    res = Solution().restoreIpAddresses(s)
    if sorted(res) == sorted(expected):
        print(test_name + ' success')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = "25525511135";
    expected1 = {
        "255.255.11.135", "255.255.111.35"
    };
    test("test1", s1, expected1);

    s2 = "010010";
    expected2 = {
        "0.10.0.10","0.100.1.0"
    };
    test("test2", s2, expected2);
