#include <iostream>
#include <stack>
using namespace std;

class CQueue {
    stack<int> s_i, s_o;
public:
    CQueue() {
        while (!s_i.empty()) s_i.pop();
        while (!s_o.empty()) s_o.pop();
    }
    
    void appendTail(int value) {
        s_i.push(value);
    }
    
    int deleteHead() {
        if (!s_o.empty()) {
            int res = s_o.top(); s_o.pop();
            return res;
        }
        if (!s_i.empty()) {
            while (!s_i.empty()) {
                int tmp = s_i.top(); s_i.pop();
                s_o.push(tmp);
            }
            int res = s_o.top(); s_o.pop();
            return res;
        }
        return -1;
    }
};

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue* obj = new CQueue();
 * obj->appendTail(value);
 * int param_2 = obj->deleteHead();
 */

void test1()
{
    CQueue q = CQueue();
    q.appendTail(3);
    int res1 = q.deleteHead();
    int res2 = q.deleteHead();

    if (res1 == 3 && res2 == -1)
        cout << "test1 success." << endl;
    else
        cout << "test1 failed." << endl;
}

int main()
{
    test1();
    return 0;
}