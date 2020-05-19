#include <iostream>
#include <vector>
#include "utils_cpp/list.h"
using namespace std;

class Solution {
public:
    vector<int> reversePrint(ListNode* head) {
        if (!head)
            return {};
        vector<int> res = reversePrint(head->next);
        res.push_back(head->val);
        return res;
    }
};


void test(string test_name, ListNode* head, vector<int> expected)
{
    vector<int> res = Solution().reversePrint(head);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    ListNode* l1 = new ListNode(1);
    l1->next = new ListNode(3);
    l1->next->next = new ListNode(2);
    vector<int> expected1 = {2,3,1};
    test("test1", l1, expected1);

    return 0;
}
