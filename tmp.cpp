#include<iostream>
#include<deque>
#include<string>
using namespace std;

class bigInteger
{
private:
    deque<int> value;
public:
    bigInteger() {}
    bigInteger(int x)
    {
        while (x) {
            value.push_front(x % 10);
            x /= 10;
        }
    }

    void print()
    {
        deque<int>::const_iterator iter;
        for (iter = value.begin(); iter != value.end(); iter++) {
            printf("%d", *iter);
        }
        printf("\n");
    }

    bigInteger operator + (bigInteger const &other) const
    {
        int carry = 0;
        bigInteger res;
        deque<int>::const_reverse_iterator iter, o_iter;
        iter = value.rbegin();
        o_iter = other.value.rbegin();

        while (iter != value.rend() || o_iter != other.value.rend() || carry) {
            int v1 = iter != value.rend() ? *iter++ : 0;
            int v2 = o_iter != other.value.rend() ? *o_iter++ : 0;

            int sum = v1 + v2 + carry;
            res.value.push_front(sum % 10);
            carry = sum / 10;
        }
        res.print();
        return res;
    }
};

int main()
{
    string str1, str2;
    while (cin >> str1) {
        cin >> str2;
        cout << str1 << " " << str2 << endl;
        bigInteger res;
        for (int i = 0; str1[i]; i++) {
            for (int j = 0; str2[j]; j++) {
                res = res + bigInteger((str1[i] - '0') * (str2[j] - '0'));
            }
        }
        res.print();
    }
    return 0;
}