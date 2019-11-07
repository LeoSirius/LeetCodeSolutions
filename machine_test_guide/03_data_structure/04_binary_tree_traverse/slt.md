### 思路1 利用三种遍历之间的关系直接输出

```cpp
#include<iostream>
#include<string>
using namespace std;

string str_pre, str_in, str_post;

void print_post(int s1, int e1, int s2, int e2)
{
    int root_idx = s2;
    while (str_pre[s1] != str_in[root_idx]) root_idx++;
    // 递归，先输出左子树，再输出右子树，再输出根结点。root_idx-s2是左边的结点的个数。
    if (root_idx != s2) print_post(s1+1, s1+(root_idx-s2), s2, root_idx-1);
    if (root_idx != e2) print_post(s1+(root_idx-s2)+1, e1, root_idx+1, e2);
    printf("%c", str_in[root_idx]);
}

int main()
{
    while (cin >> str_pre) {
        cin >> str_in;
        print_post(0, str_pre.size()-1, 0, str_in.size()-1);
        printf("\n");
    }
    return 0;
}
```
