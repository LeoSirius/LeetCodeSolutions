# 例2_又一版A+B

**题目描述：**

```
输入两个不超过整形定义的非负10进制整数A和B（ <= 2^31-1）。输出A+B的m进制数。1 <= m <= 10
```

**输入：**

```
包含多个测试用例。每个测试用例占一行，分别为m、A和B
```

**输出：**

```
每个输出占一行
```

**输入样例：**

```
8 1300 48
2 1 7
0
```

**输出样例：**

```
2504
1000
```



**思路：**

```

```



**代码：**

```c++
#include<stdio.h>

int main(){
	long long a, b;
	int m;
	while (scanf("%d", &m) != EOF) {
		if (m == 0) break;
		scanf("%lld%lld", &a, &b);
		a += b;
		int ans[50], size = 0;
		do {						//注意这个循环求出来是从低位到高位，所以下面反向输出
			ans[size++] = a % m;
			a /= m;
		} while (a != 0);
		for (int i = size - 1; i >= 0; i--)
			printf("%d", ans[i]);
		printf("\n");
	}
	return 0;
}
```

