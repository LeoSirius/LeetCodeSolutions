#include<iostream>
#include<deque>
using namespace std;

class BigInteger
{
private:
    deque<int> value;
public:
    BigInteger() {};
    BigInteger(int x)
    {
        while (x) {
            value.push_front(x % 10);
            x /= 10;
        }
    }

    void print () const
    {
        deque<int>::const_iterator iter = value.begin();
        for (; iter != value.end(); iter++)
            printf("%d", *iter);
        printf("\n");
    }

    bool is_zero()
    {   
        cout << "value.size() = " << value.size() << endl;
        return !value.size() || (value.size() == 1 && value[0] == 0);
    }

    BigInteger operator + (BigInteger const &other) const
    {
        int carry = 0;
        BigInteger res;
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
        return res;
    }

    BigInteger operator * (int k) const
    {
        int carry = 0;
        BigInteger res;
        deque<int>::const_reverse_iterator iter = value.rbegin();
        while (iter != value.rend() || carry) {
            int v = iter != value.rend() ? *iter++ : 0;
            int mul = v * k + carry;
            res.value.push_front(mul % 10);
            carry = mul / 10;
        }
        return res;
    }

    BigInteger operator / (int k) const
    {
        int remainder = 0;
        BigInteger res;
        deque<int>::const_iterator iter = value.begin();
        for (; iter != value.end(); iter++) {
            int cur_dvd = remainder * 10 + *iter;
            int cur_res = cur_dvd / k;
            remainder = cur_dvd % k;
            res.value.push_back(cur_res);
        }
        while(res.value.size() && res.value[0] == 0) res.value.pop_front();
        return res;
    }

    int operator % (int k) const
    {
        int remainder = 0;
        deque<int>::const_iterator iter = value.begin();
        for (; iter != value.end(); iter++)
        {
            int cur_dividend = remainder * 10 + *iter;
            remainder = cur_dividend % k;
        }
        return remainder;
    }



};

int main()
{
    int m, n;
    while (scanf("%d %d", &m, &n) != EOF) {
        string x;
        cin >> x;

        BigInteger decimal(0);
        BigInteger base(1);
        for (int i = x.size() - 1; i >= 0; i--) {
            int cur_num;
            if (x[i] >= '0' && x[i] <= '9') cur_num = x[i] - '0';
            else cur_num = x[i] - 'A' + 10;
            decimal = decimal + (base * cur_num);
            base = base * m;
            cout << cur_num << endl;
        }
        decimal.print();
        cout << "===" << endl;

        deque<char> res;
        do {
            decimal.print();
            int mod = decimal % n;
            res.push_front("0123456789ABCDEF"[mod]);
            decimal = decimal / n;
        } while (!decimal.is_zero());
        cout << "22" << endl;
        deque<char>::const_iterator iter;
        for (iter = res.begin(); iter != res.end(); iter++) {
            printf("%c", *iter);
        }
        printf("\n");
    }
    return 0;
}