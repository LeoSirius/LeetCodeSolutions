#include<iostream>
#include<deque>
using namespace std;

class bigInteger
{
private:
    deque<int> value;

public:
    bigInteger () {};
    bigInteger (int x);

    void print () const;
    bool is_zero () const;

    bigInteger operator+ (const bigInteger& B) const;
    bigInteger operator* (int x) const;
    bigInteger operator/ (int x) const;
    int operator% (int x) const;
};

bigInteger::bigInteger (int x)
{
    while (x)
    {
        value.push_front(x % 10);
        x /= 10;
    }
}

void bigInteger::print () const
{
    deque<int>::const_iterator iter = value.begin();
    for (; iter != value.end(); iter++)
        printf("%d", *iter);
    printf("\n");
}

bool bigInteger::is_zero () const
{
    return !value.size() || (value.size() == 1 && value[0] == 0);
}

bigInteger bigInteger::operator+ (const bigInteger& B) const
{
    bigInteger res;
    int carry = 0;
    deque<int>::const_reverse_iterator iter = value.rbegin(), iter_B = B.value.rbegin();
    while (iter != value.rend() || iter_B != B.value.rend() || carry)
    {
        int v1, v2;
        v1 = v2 = 0;
        if (iter != value.rend())
        {
            v1 = *iter;
            iter++;
        }
        if (iter_B != B.value.rend())
        {
            v2 = *iter_B;
            iter_B++;
        }
        int sum = v1 + v2 + carry;
        res.value.push_front(sum % 10);
        carry = sum / 10;
    }
    return res;
}

bigInteger bigInteger::operator* (int x) const
{
    bigInteger res;
    int carry = 0;
    deque<int>::const_reverse_iterator iter = value.rbegin();
    for (; iter != value.rend(); iter++)
    {
        int multiple = *iter * x + carry;
        res.value.push_front(multiple % 10);
        carry = multiple / 10;
    }
    if (carry) res.value.push_front(carry);
    return res;
}

bigInteger bigInteger::operator/ (int x) const
{
    bigInteger res;
    int remainder = 0;
    deque<int>::const_iterator iter = value.begin();
    for (; iter != value.end(); iter++)
    {
        int cur_dividend = remainder * 10 + *iter;
        int cur_res = cur_dividend / x;
        remainder = cur_dividend % x;
        res.value.push_back(cur_res);
    }
    while(res.value.size() && res.value[0] == 0) res.value.pop_front();
    return res;
}

int bigInteger::operator% (int x) const
{
    int remainder = 0;
    deque<int>::const_iterator iter = value.begin();
    for (; iter != value.end(); iter++)
    {
        int cur_dividend = remainder * 10 + *iter;
        remainder = cur_dividend % x;
    }
    return remainder;
}

int main ()
{
    int m, n;
    while (scanf("%d %d", &m, &n) != EOF)
    {
        string x_str;
        cin >> x_str;
        bigInteger big_decimal, base(1);

        for (int i = x_str.size() - 1; i >= 0; i--)
        {
            int cur_num;
            if (x_str[i] >= '0' && x_str[i] <= '9')
                cur_num = x_str[i] - '0';
            else
                cur_num = x_str[i] - 'A' + 10;
            big_decimal = big_decimal + base * cur_num;
            base = base * m;
        }

        int size = 0;
        char res[100000];
        do {
            int mod = big_decimal % n;
            if (mod >= 10) res[size++] = mod - 10 + 'A';
            else res[size++] = mod + '0';
            big_decimal = big_decimal / n;
        } while (!big_decimal.is_zero());

        for(int i = size - 1; i >= 0; i--) printf("%c", res[i]);
        printf("\n");
    }
    return 0;
}