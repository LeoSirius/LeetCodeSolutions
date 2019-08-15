#include<iostream>
#include<deque>
using  namespace std;

class bigInteger
{
private:
    deque<int> value;

public:
    bigInteger () {};
    bigInteger (int x)
    {
        while (x)
        {
            value.push_front(x % 10);
            x /= 10;
        }
    }

    void print ()
    {
        deque<int>::const_iterator iter = value.begin();
        for (; iter != value.end(); iter++)
        {
            printf("%d", *iter);
        }
        printf("\n");
    }

    bigInteger operator * (int x) const
    {
        bigInteger res;
        int carry = 0;
        deque<int>::const_reverse_iterator iter = value.rbegin();
        while (iter != value.rend() || carry)
        {
            int v1 = 0;
            if (iter != value.rend())
            {
                v1 = *iter;
                iter++;
            }
            int multiple = v1 * x + carry;
            res.value.push_front(multiple % 10);
            carry = multiple / 10;
        }
        return res;
    }
    friend istream& operator >> (istream& is, bigInteger& bigInt);
};

istream& operator >> (istream& is, bigInteger& bigInt)
{
    string s;
    cin >> s;
    bigInt.value.clear();
    for (int i = 0; s[i]; i++)
    {
        bigInt.value.push_back(s[i] - '0');
    }
    return is;
}

int main ()
{
    int n;
    while (scanf("%d", &n) != EOF)
    {
        bigInteger res(1);
        for (int i = 2; i <= n; i++)
        {
            res = res * i;
        }
        res.print();
    }
    return 0;
}