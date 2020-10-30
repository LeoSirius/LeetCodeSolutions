#include <iostream>
#include <unordered_map>
#include <set>
using namespace std;

struct Node
{
    int freq;
    int time;      // last access time
    int key, value;

    Node (int f, int t, int k, int v): freq(f), time(t), key(k), value(v){}

    // set是实现了红黑树平衡二叉搜索树，插入元素时，它会自动调整二叉树的排列，
    // 把元素放到适当的位置，以保证每个子树根节点键值大于左子树所有节点的键值，小于右子树所有节点的键值；
    // 另外，还得保证根节点左子树的高度与右子树高度相等。
    // 这里重载比较运算符
    bool operator< (const Node& other) const
    {
        // 返回freq小的，如果频率相同，则返回last access time在之前的
        return freq == other.freq ? time < other.time : freq < other.freq;
    }
};

class LFUCache {
    int capacity, time;
    unordered_map<int, Node> k_node_mp;
    set<Node> node_set;
public:
    LFUCache(int _capacity) {
        capacity = _capacity;
        time = 0;
        k_node_mp.clear();
        node_set.clear();
    }
    
    int get(int key) {
        if (capacity == 0)
            return -1;

        // 没找到，返回-1
        auto iter = k_node_mp.find(key);
        if (iter == k_node_mp.end())
            return -1;
        
        // 从hash表中得到旧结点，并在搜索树中删除
        Node node = iter->second;
        node_set.erase(node);

        // 更新就缓存
        node.freq += 1;
        node.time = ++time;

        // 重新写回搜索树和hahs表中，
        node_set.insert(node);
        iter->second = node;

        return node.value;
    }
    
    void put(int key, int value) {
        if (capacity == 0)
            return;

        auto iter = k_node_mp.find(key);
        if (iter == k_node_mp.end()) {
            // 原hash表中没有，插入新结点
            if (k_node_mp.size() == capacity) {
                k_node_mp.erase(node_set.begin()->key);
                node_set.erase(node_set.begin());
            }
            Node node = Node(1, ++time, key, value);
            k_node_mp.insert(make_pair(key, node));
            node_set.insert(node);
        } else {
            // 原hash表中有，更改原结点的值和freq、time信息
            Node node = iter->second;
            node_set.erase(node);

            node.freq += 1;
            node.time = ++time;
            node.value = value;

            node_set.insert(node);
            iter->second = node;
        }
    }
};

void test(string test_name)
{
    LFUCache *obj = new LFUCache(2);
    bool is_correct = true;

    // cache.put(1, 1);
    // cache.put(2, 2);
    // cache.get(1);       // returns 1
    // cache.put(3, 3);    // evicts key 2
    // cache.get(2);       // returns -1 (not found)
    // cache.get(3);       // returns 3.
    // cache.put(4, 4);    // evicts key 1.
    // cache.get(1);       // returns -1 (not found)
    // cache.get(3);       // returns 3
    // cache.get(4);       // returns 4
    obj->put(1, 1);
    obj->put(2, 2);
    if (obj->get(1) != 1)
        is_correct = false;
    obj->put(3, 3);
    if (obj->get(2) != -1)
        is_correct = false;
    if (obj->get(3) != 3)
        is_correct = false;
    obj->put(4,4);
    if (obj->get(1) != -1)
        is_correct = false;
    if (obj->get(3) != 3)
        is_correct = false;
    if (obj->get(4) != 4)
        is_correct = false;

    if (is_correct) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }

}

int main()
{
    test("test1");
    return 0;
}