#include <iostream>
#include <vector>
using namespace std;


class Node {
public:
    int val;
    vector<Node*> neighbors;
    
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
    Node* visited[101] = {nullptr};   // 注意这里存的是clone的结点，不是原结点
public:
    Node* cloneGraph(Node* node) {
        if (!node)
            return nullptr;

        int cur_neighbor_cnt = node->neighbors.size();

        Node *new_node = new Node(node->val);  // neighbor初始化为空vector
        visited[node->val] = new_node;

        for (int i = 0; i < cur_neighbor_cnt; i++) {
            Node *neighbor = node->neighbors[i];
            if (!visited[neighbor->val])
                // 邻居没访问过，继续dfs。new新的结点
                new_node->neighbors.push_back(cloneGraph(neighbor));
            else
                // 邻居访问过，已经new过，直接加到neighbor中
                new_node->neighbors.push_back(visited[neighbor->val]);
        }

        return new_node;
    }
};

int main()
{
    // 暂时不测
    return 0;
}