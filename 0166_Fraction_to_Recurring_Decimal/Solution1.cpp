#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (!numerator)
            return "0";
        string res = "";
        if (numerator > 0 ^ denominator > 0)
            res += "-";
        
        long long n = abs((long long)numerator), d = abs((long long)denominator), r = n % d;
        res += to_string(n / d);
        if (!r) {
            return res;
        }
        res += ".";

        unordered_map<long long, int> mp;
        while (r) {
            if (mp.find(r) != mp.end()) {
                res.insert(mp[r], "(");
                res += ')';
                return res;
            }
            mp[r] = res.size();
            r *= 10;
            res += to_string(r / d);
            r %= d;
        }
        return res;
    }
};


void test(string test_name, int numerator, int denominator, string expected)
{
    string res = Solution().fractionToDecimal(numerator, denominator);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int numerator1 = 1;
    int denominator1 = 2;
    string expected1 = "0.5";
    test("test1", numerator1, denominator1, expected1);

    int numerator2 = 2;
    int denominator2 = 1;
    string expected2 = "2";
    test("test2", numerator2, denominator2, expected2);

    int numerator3 = 2;
    int denominator3 = 3;
    string expected3 = "0.(6)";
    test("test3", numerator3, denominator3, expected3);

    int numerator4 = 4;
    int denominator4 = 333;
    string expected4 = "0.(012)";
    test("test4", numerator4, denominator4, expected4);

    return 0;
}
