**思路：**

```

```



**c\c++代码：**

```c++
#include<cstdio>
#include<cstring>
#include<cstdlib>

// ====================方法一====================   不断除10来判断每位  O(nlongn)
int NumberOf1(unsigned int n);

int NumberOf1Between1AndN_Solution1(unsigned int n) {
	int number = 0;
	for (unsigned int i = 1; i <= n; i++)
		number += NumberOf1(n);
	return number;
}

int NnumberOf1(unsigned int n) {
	int number = 0;
	while (n) {
		if (n % 10 == 1)
			number++;
		n /= 10;
	}
	return number;
}

// ====================方法二====================  可暂时不管
int NumberOf1(const char* strN);
int PowerBase10(unsigned int n);

int NumberOf1Between1AndN_Solution2(int n)
{
	if (n <= 0)
		return 0;

	char strN[50];
	sprintf(strN, "%d", n);

	return NumberOf1(strN);
}

int NumberOf1(const char* strN) {
	if (!strN || *strN < '0' || *strN > '9' || *strN == '\0')
		return 0;

	int first = *strN - '0';
	unsigned int length = static_cast<unsigned int>(strlen(strN));
	if (length == 1 && first == 0)
		return 0;
	if (length == 1 && first > 0)
		return 1;

	int numFirstDigit = 0;
	if (first > 1)
		numFirstDigit = PowerBase10(length - 1);
	else if (first == 1)
		numFirstDigit = atoi(strN + 1) + 1;

	// numOtherDigits是01346-21345除了第一位之外的数位中1的数目
	int numOtherDigits = first * (length - 1) * PowerBase10(length - 2);
	// numRecursive是1-1345中1的数目
	int numRecursive = NumberOf1(strN + 1);

	return numFirstDigit + numOtherDigits + numRecursive;
}

int PowerBase10(unsigned int n) {
	int result = 1;
	for (unsigned int i = 0; i < n; i++)
		result *= 10;
	return result;
}

// ====================测试代码====================
void Test(const char* testName, int n, int expected)
{
	if (testName != nullptr)
		printf("%s begins: \n", testName);

	if (NumberOf1Between1AndN_Solution1(n) == expected)
		printf("Solution1 passed.\n");
	else
		printf("Solution1 failed.\n");

	if (NumberOf1Between1AndN_Solution2(n) == expected)
		printf("Solution2 passed.\n");
	else
		printf("Solution2 failed.\n");

	printf("\n");
}

void Test()
{
	Test("Test1", 1, 1);
	Test("Test2", 5, 1);
	Test("Test3", 10, 2);
	Test("Test4", 55, 16);
	Test("Test5", 99, 20);
	Test("Test6", 10000, 4001);
	Test("Test7", 21345, 18821);
	Test("Test8", 0, 0);
}

int main(int argc, char* argv[])
{
	Test();

	return 0;
}
```

**python代码：**

```python

```

