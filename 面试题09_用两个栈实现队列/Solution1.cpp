#include <iostream>
#include <stack>
using namespace std;

class CQueue {
    stack<int> s_in, s_out;
public:
    CQueue() {
        while (!this->s_in.empty()) this->s_in.pop();
        while (!this->s_out.empty()) this->s_out.pop();
    }
    
    void appendTail(int value) {
        this->s_in.push(value);
    }
    
    int deleteHead() {
        if (!this->s_out.empty()) {
            int res = this->s_out.top();
            this->s_out.pop();
            return res;
        } else {
            if (this->s_in.empty())
                return -1;
            while (!this->s_in.empty()) {
                int tmp = this->s_in.top(); this->s_in.pop();
                this->s_out.push(tmp);
            }
            int res = this->s_out.top();
            this->s_out.pop();
            return res;
        }
    }
};

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
