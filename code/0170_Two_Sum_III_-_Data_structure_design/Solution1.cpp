#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class TwoSum {
    unordered_map<int, int> mp;
public:
    /** Initialize your data structure here. */
    TwoSum() {
        
    }
    
    /** Add the number to an internal data structure.. */
    void add(int number) {
        ++mp[number];
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    bool find(int value) {
        for (auto pair : mp) {
            int num_to_find = value - pair.first;
            if (num_to_find == pair.first && pair.second > 1)
                return true;
            if (num_to_find != pair.first && mp.find(num_to_find) != mp.end())
                return true;
        }
        return false;
    }
};

void test1()
{
    TwoSum ts;
    ts.add(1);
    ts.add(3);
    ts.add(5);
    if (ts.find(4) == true && ts.find(7) == false) {
        cout << "test1 success." << endl;
    } else {
        cout << "test1 failed." << endl;
    }
}

void test2()
{
    TwoSum ts;
    ts.add(3);
    ts.add(1);
    ts.add(2);
    // cout << "ts.find(6) = " << ts.find(6) << endl;
    if (ts.find(3) == true && ts.find(6) == false) {
        cout << "test2 success." << endl;
    } else {
        cout << "test2 failed." << endl;
    }
}

void test3()
{
    TwoSum ts;
    ts.add(0);
    ts.add(0);
    if (ts.find(0) == true) {
        cout << "test3 success." << endl;
    } else {
        cout << "test3 failed." << endl;
    }
}

int main()
{
    test1();
    test2();
    test3();
    return 0;
}
