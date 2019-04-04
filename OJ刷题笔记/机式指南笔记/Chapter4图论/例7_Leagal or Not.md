# 例7_Leagal or Not

**题目描述：**

```
ACM-DIY is a large QQ group where many excellent acmers get together. It is so harmonious that just like a big family. Every day, many 'holy cows' like HH, hh, AC and so on chat on-line to exchange their ideas. When someone has questions, many warm-hearted cows like Lost will come to help. Then the one being helped will call Lost 'master', and Lost will have a nice 'pretice'. By and by, there are many pairs of 'masters and prentices'. But then problem occurs: there are too many masters and to many prentices, how can we know whether it is legal or not? 
We all know a master can have many prentices and a prentice may have a lot of masters too, it's legal. Nevertheless, some cows are not so honest, they hold illegal relationship. Take HH and 3xian for instance, HH is 3xian's master and, at the same time, 3xian is HH's master, which is quite illegal! To avoid this, please help us to judge whether their relationship is legal or not. 
Please note that the 'masster and prentice' is transitive. It means that if A is B's master and B is C's master, then A is C's master.
```

**输入：**

```
The input consists of several test caese. For each case, the first line contains two integers, N(members to be tested) and M(relationships to be tested)(2 <= N, M <= 100). Then M lines follow, each contains a pair of (x, y) which means x is y's master and y is x's prentice. The input is terminated my N = 0. To make it simple, we give every one a number(0,1,2,3,...N-1). We use their numbers instead of their names.
```

**输出：**

```
For each test case, print in one line the judgement of the messy relationship. If it is legal, output "YES", otherwise "NO".
```

**输入样例：**

```
3 2 
0 1
1 2
2 2 
0 1
1 0
0 0
```

**输出样例：**

```
YES
NO
```



**思路：**

```
将所有的师徒关系抽象成有向边（由师父指向徒弟），该问题即转化为判断该图是否是有向无环图。
```



**代码：**

```c++
#include<stdio.h>
#include<vector>
#include<queue>
using namespace std;

vector<int> edge[501];		//邻接链表，边不存在权值，所以只用保存邻接的结点的编号即可
queue<int> Q;				//保存入度为0的结点的队列

int main() {
	int inDegree[501];		//统计每个结点的入度
	int n, m;
	while (scanf("%d%d", &n, &m) != EOF) {
		if (n == 0 && m == 0) break;
		for (int i = 0; i < n; i++) {		//初始化所有结点
			inDegree[i] = 0;
			edge[i].clear();
		}
		while (m--) {
			int a, b;
			scanf("%d%d", &a, &b);
			inDegree[b]++;			//指向b的边，b入度加1
			edge[a].push_back(b);
		}

		while (Q.empty() == false) Q.pop();		//清空队列

		for (int i = 0; i < n; i++)
			if (inDegree[i] == 0)
				Q.push(i);				//将入度为0的结点放入队列

		int cnt = 0;		//累计已经确定拓扑序列的结点的个数
		while (Q.empty() == false) {
			int newP = Q.front(); Q.pop();
			cnt++;
			for (int i = 0; i < edge[newP].size(); i++) {
				inDegree[edge[newP][i]]--;
				if (inDegree[edge[newP][i]] == 0)
					Q.push(edge[newP][i]);
			}
		}
		if (cnt == n) puts("YES");		//所有结点都能被确定拓扑序列，则原图为有向无环图
		else puts("NO");
	}
	return 0;
}

```

