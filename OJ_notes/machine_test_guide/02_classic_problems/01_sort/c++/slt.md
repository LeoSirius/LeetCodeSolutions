## 思路1 用内置sort排序

内置`sort`是用的快排实现，n*logn的复杂度

```cpp
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        vector<int> input_array;
        int tmp;
        for(int i = 0; i < n; i++){
            scanf("%d", &tmp);
            input_array.push_back(tmp);
        }
        sort(input_array.begin(), input_array.end());

        // no space after laster number, so treat it alone
        for(int i = 0; i < input_array.size() - 1; i++){
            printf("%d ", input_array[i]);
        }
        printf("%d", input_array[input_array.size()-1]);
        printf("\n");
    }
    return 0;
}
```