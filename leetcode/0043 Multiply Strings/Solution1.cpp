#include<iostream>
#include<string>
using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {
        string product(num1.size() + num2.size(), '0');
        
        for (int i = num1.size() - 1; 0 <= i; --i) {
            int carry = 0;
            for (int j = num2.size() - 1; 0 <= j; --j) {
                int tmp = (product[i + j + 1] - '0') + (num1[i] - '0') * (num2[j] - '0') + carry;
                product[i + j + 1] = tmp % 10 + '0';
                carry = tmp / 10;
            }
            product[i] += carry;
        }

        size_t startpos = product.find_first_not_of("0");
        if (string::npos != startpos) {
            return product.substr(startpos);
        }
        return "0";
    }
};


// ====================测试代码====================
void test(string testName, string num1, string num2, string res)
{
    Solution s;
    if(res == s.multiply(num1, num2)){
        cout << testName << " success." << endl;
    } else {
        cout << testName << " failed." << endl;
    }
}

void test1()
{
    test("test1", "2", "3", "6");
}

void test2()
{
    test("test1", "123", "456", "56088");
}

int main()
{
    //test1();
    test2();
    return 0;
}