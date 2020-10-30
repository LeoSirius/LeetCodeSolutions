#include <iostream>
#include <unordered_map>
#include <list>
using namespace std;

class LRUCache {
private:
    int _capacity;

    // table的键就是k，值是list结点的指针
    unordered_map<int, list<pair<int, int>>::iterator> _table;

    // list保存kv対，get过后，放到最前面。最后一个即lru
    list<pair<int, int>> _list;
public:
    LRUCache(int capacity) {
        _capacity = capacity;
    }
    
    int get(int key) {
        auto it = _table.find(key);
        if (it == _table.end()) return -1;

        // get的时候，把这个结点移动到最前面
        // it指向的是table，it->second即是list中目标结点的指针
        // 把第二个参数的list中的第三个参数指向的结点，移动到第一个_list的第一个结点。
        _list.splice(_list.begin(), _list, it->second);
        return it->second->second;
    }
    
    void put(int key, int value) {
        auto it = _table.find(key);

        // key已存在，则replace旧的。并更新list
        if (it != _table.end()) {
            _list.splice(_list.begin(), _list, it->second);
            it->second->second = value;
            return;
        }

        // key不存在，则在头部插入。如果list大小超过capacity，则去掉最后一个
        _list.emplace_front(key, value);
        _table[key] = _list.begin();      // 同时更新table

        if (_capacity < _table.size()) {
            _table.erase(_list.back().first);
            _list.pop_back();
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

void test1()
{
    LRUCache *cache = new LRUCache(2);
    cache->put(1, 1);
    cache->put(2, 2);
    int res1 = cache->get(1);       // 1
    cache->put(3, 3);               // evicts key 2
    int res2 = cache->get(2);       // -1
    cache->put(4, 4);               // evicts key 1
    int res3 = cache->get(1);       // -1
    int res4 = cache->get(3);       // 3
    int res5 = cache->get(4);       // 4

    if (res1 == 1 && res2 == -1 && res3 == -1 && res4 == 3 && res5 == 4)
        cout << "test1 success." << endl;
    else
        cout << "test1 failed." << endl;
}

int main()
{
    test1();

    return 0;
}



// Design and implement a data structure for Least Recently Used (LRU) cache. 
// It should support the following operations: get and put.

// get(key) - Get the value (will always be positive) of the key 
// if the key exists in the cache, otherwise return -1.
// put(key, value) - Set or insert the value if the key is not already present. 
// When the cache reached its capacity, it should invalidate the least recently 
// used item before inserting a new item.

// The cache is initialized with a positive capacity.

// Follow up:
// Could you do both operations in O(1) time complexity?

// Example:

// LRUCache cache = new LRUCache( 2 /* capacity */ );

// cache.put(1, 1);
// cache.put(2, 2);
// cache.get(1);       // returns 1
// cache.put(3, 3);    // evicts key 2
// cache.get(2);       // returns -1 (not found)
// cache.put(4, 4);    // evicts key 1
// cache.get(1);       // returns -1 (not found)
// cache.get(3);       // returns 3
// cache.get(4);       // returns 4

