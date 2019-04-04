# 例4_Freckles

**题目描述：**

```
In an episode of the Dick Van Dyke show, little Richie connets the freckles on his Dad's back to form a picture of the Liberty Bell. Alas, one of the freckles turns out to be a scar, so his Ripley's engagement falls through. 
Consider Dick's back to be a plane with freckles at various(x,y) locations. Your job is to tell Richie how to connect the dots so as to minimize the amount of link used. Richie connets the dots by drawing straight lines between pairs, possibly lifting the pen between lines. When Richie is done there must be a sequence of connected lines from any freckle to any other freckle.
```

**输入：**

```
The first line contains 0 < n <= 100, the number of freckles on Dick's back. For each freckle, a line follows; each following line contains two real numbers indicating the(x,y) coordinates of the freckle.
```

**输出：**

```
Your program prints a single real number t two decimal places: the minimum total length of ink lines that can connect all the freckles.
```

**输入样例：**

```
3
1.0 1.0
2.0 2.0
2.0 4.0
```

**输出样例：**

```
3.41
```



**思路：**

```
这是一道含蓄的最小生成树问题。
题目大意为平面上有若干个点，我们需要用一些线段将这些点连接起来，使任意两个点能够通过一系列的线段相连。给出所有的点的坐标，求一种连接方式使所有线段的长度之和最小，求该长度和。
```



**代码：**

```c++
#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;

#define N 101

int Tree[N];

int FindRoot(int x) {
	if (Tree[x] == -1) return x;
	else {
		int tmp = FindRoot(Tree[x]);
		Tree[x] = tmp;
		return tmp;
	}
}

struct Edge {
	int a, b;
	double cost;
	bool operator < (const Edge &A)const {
		return cost < A.cost;
	}
}edge[6000];

struct Point {
	double x, y;
	double GetDistance(Point A) {
		double tmp = (x - A.x) * (x - A.x) + (y - A.y) * (y - A.y);
		return sqrt(tmp);
	}
}list[101];

int main() {
	int n;
	while (scanf("%d", &n) != EOF) {
		for (int i = 1; i <= n; i++) {
			scanf("%lf%lf", &list[i].x, &list[i].y);
		}
		int size = 0;					//边的总数
		for (int i = 1; i <= n; i++) {	//可以考虑看成一个无向图，只存上三角
			for (int j = i + 1; j <= n; j++) {
				edge[size].a = i;
				edge[size].b = j;
				edge[size].cost = list[i].GetDistance(list[j]);
				size++;
			}
		}

		sort(edge, edge + size);
		for (int i = 1; i <= n; i++)
			Tree[i] = -1;
		double ans = 0;
		for (int i = 0; i < size; i++) {
			int a = FindRoot(edge[i].a);
			int b = FindRoot(edge[i].b);
			if (a != b) {
				Tree[a] = b;
				ans += edge[i].cost;
			}
		}
		printf("%.2lf\n", ans);
	}
	return 0;
}
```

