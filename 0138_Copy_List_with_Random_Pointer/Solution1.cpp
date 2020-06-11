#include <iostream>
#include <vector>
using namespace std;

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
        Node *p = head;
        // copy node without random
        // 用next连接p和copy出来的新节点。
        while (p) {
            Node *node = new Node(p->val, p->next, nullptr);
            p->next = node;
            p = node->next;
        }

        p = head;
        while (p) {         // 连接random
            if (p->random) p->next->random = p->random->next;
            p = p->next->next;
        }

        Node* res = head->next;
        p = head;
        while (p->next) {   // 有丝分裂(大雾)
            Node *tmp = p->next;
            p->next = p->next->next;
            p = tmp;
        }
        return res;
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
    // 7 -> 13 -> 11 -> 10 -> 1
    // random
    // 31 -> 7
    // 11 -> 1
    // 10 -> 11
    // 1 -> 7
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

