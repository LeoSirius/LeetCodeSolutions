# 例2_More is better

**题目描述：**

```
Mr Wang wants some boys to help him with a project. Because the project is rather complex, the more boys come, the better it will be. Of course there are certain requirements. Mr Wang selected a room big enough to hold the boys. The boy who are not been chosen has to leave the room immediately. There are 10,000,000 boys in the room numbered from 1 to 10,000,000 at the very beginning. After Mr Wang's selection any two of them who are still in this room should be friends(direct or indirect), or there is only one boy left. Given all the direct firend-pairs, you should decide the best way.
```

**输入：**

```
The first lone of the input contains an integer n (0 <= n <= 100,000) -the number of direct friend-pairs. The following n lines each contains a pair of numbers A and B separated by a single space that suggests A and B are direct friends. (A != B, 1 <= A,B <= 10,000,000)
```

**输出：**

```
the output in one line contains exactly one integer equals to the maximum number of boys Mr Wang may keep.
```

**输入样例：**

```
4
1 2
3 4
5 6
1 6
4 
1 2
3 4
5 6
7 8
```

**输出样例：**

```
4
2
```



**思路：**

```
题目要求我们找出人数最多的一个集合，并输出集合中元素的个数。
仍然用并查集完成，新加一个数组来统计每个集合中有多少个元素。
```



**代码：**

```c++
#include<stdio.h>
using namespace std;
#define N 10000001

int Tree[N];
int sum[N];		//用sum[i]保存以结点i为根的树的结点个数，其中保存数据当且仅当Tree[i]为-1时有效

int FindRoot(int x){
	if(Tree[x] == -1) return x;
	else{
		int tmp = FindRoot(Tree[x]);
		Tree[x] = tmp;
		return tmp;
	}
} 

int main(){
	int n;
	while(scanf("%d", &n) != EOF){
		for(int i = 1; i <N; i++){
			Tree[i] = -1;
			sum[i] = 1;
		}
		while(n--){
			int a, b;
			scanf("%d%d", &a, &b);
			a = FindRoot(a);
			b = FindRoot(b);
			if(a != b){
				Tree[a] = b;
				sum[b] += sum[a];
			}
		}
		int ans = 1;
		for(int i = 1; i <= N; i++){
			if(Tree[i] == -1 && sum[i] > ans) ans = sum[i];
		}
		printf("%d\n", ans);
	}
	return 0;
}
```

