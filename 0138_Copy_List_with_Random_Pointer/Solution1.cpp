#include <iostream>
#include <vector>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int x, Node* next=nullptr, Node* random=nullptr) : val(x), next(next), random(random) {}
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;
        Node* ite = head;
        while (ite) { // 用next连接   // copy node without random
            Node* n = new Node(ite->val, ite->next, nullptr);
            Node* c = ite->next;
            ite->next = n;
            ite = c;
            
        }
        ite = head;
        while (ite) { // 连接random
            if (ite->random) ite->next->random = ite->random->next;
            ite = ite->next->next;
        }
        ite = head;

        Node* ret = head->next;
        while (ite->next) { // 有丝分裂(大雾)
            Node* c = ite->next;
            ite->next = ite->next->next;
            ite = c;
        }

        return ret;
    }
};

void test(string test_name, Node *head)
{
    Solution s;
    Node *res = s.copyRandomList(head);
    vector<int> res_nums, expected_nums;
    Node *p = res;
    while (p) {
        res_nums.push_back(p->val);
        p = p->next;
    }
    p = head;
    while (p) {
        expected_nums.push_back(p->val);
        p = p->next;
    }

    if (res_nums == expected_nums) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    Node* a0 = new Node(7);
    Node* a1 = new Node(13);
    Node* a2 = new Node(11);
    Node* a3 = new Node(10);
    Node* a4 = new Node(1);
    a0->next = a1; a1->next = a2; a2->next = a3; a3->next = a4;
    a1->random = a0;
    a2->random = a4;
    a3->random = a2;
    a4->random = a0;
    test("test1", a0);

}


