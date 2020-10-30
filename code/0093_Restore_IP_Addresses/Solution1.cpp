#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> res;
        for (int lena = 1; lena <= 3; lena++)
        for (int lenb = 1; lenb <= 3; lenb++)
        for (int lenc = 1; lenc <= 3; lenc++)
        for (int lend = 1; lend <= 3; lend++) {
            if (lena + lenb + lenc + lend == s.size()) {
                int A = stoi(s.substr(0, lena));
                if (A > 255) continue;
                int B = stoi(s.substr(lena, lenb));
                if (B > 255) continue;
                int C = stoi(s.substr(lena+lenb, lenc));
                if (C > 255) continue;
                int D = stoi(s.substr(lena+lenb+lenc, lend));
                if (D > 255) continue;
                string str = to_string(A)+"."+to_string(B)+"."+to_string(C)+"."+to_string(D);
                if(str.size() == s.size()+3) {
                    res.push_back(str);
                }
            }
        }
        return res;
    }
};

void test(string test_name, string s, vector<string> expected)
{
    Solution slt;
    vector<string> res = slt.restoreIpAddresses(s);
    sort(res.begin(), res.end());
    sort(expected.begin(), expected.end());
    for(auto item : res) {
        cout << item << endl;
    }
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "25525511135";
    vector<string> expected1 = {
        "255.255.11.135", "255.255.111.35"
    };
    test("test1", s1, expected1);

    string s2 = "010010";
    vector<string> expected2 = {
        "0.10.0.10","0.100.1.0"
    };
    test("test2", s2, expected2);

    return 0;
}
