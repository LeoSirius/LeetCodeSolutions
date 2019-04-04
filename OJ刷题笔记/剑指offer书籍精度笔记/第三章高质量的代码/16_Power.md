**思路：**

```
考虑到指数可能为负。
若底数是0，且指数为负，这时底数不能求导！
另外在除2和判断奇偶的求模用了位运算，效率更高。
这里用的公式，高效求幂：
a^n = a^n/2 * a^n/2                   n为偶数
      a^(n-1)/2 * a^(n-1)/2 * a		  n为奇数
      
函数接口：
double Power(double base, int exponent) {

}
```



**c\c++代码：**

```c++
#include<iostream>
#include<cmath>
using namespace std;

bool g_InvalidInput = false;
bool equal(double num1, double num2);
double PowerWithUnsignedExponent(double base, unsigned int exponent);

double Power(double base, int exponent) {
	g_InvalidInput = false;

	if (equal(base, 0.0) && exponent < 0) {
		g_InvalidInput = true;
		return 0.0;
	}

	unsigned int absExponent = (unsigned int)(exponent);
	if (exponent < 0)
		absExponent = (unsigned int)(-exponent);

	double result = PowerWithUnsignedExponent(base, absExponent);
	if (exponent < 0)
		result = 1.0 / result;
	return result;
}

double PowerWithUnsignedExponent(double base, unsigned int exponent) {
	if (exponent == 0)
		return 1;
	if (exponent == 1)
		return base;

	double result = PowerWithUnsignedExponent(base, exponent >> 1);
	result *= result;
	if ((exponent & 0x1) == 1)
		result *= base;
	return result;
}

bool equal(double num1, double num2) {
	if ((num1 - num2 > -0.0000001) && (num1 - num2 < 0.0000001))
		return true;
	else
		return false;
}

//========================测试代码========================
void Test(const char* testName, double base, int exponent, double expectedResult, bool expectedFalg) {
	double result = Power(base, exponent);
	if (equal(result, expectedResult) && g_InvalidInput == expectedFalg)
		cout << testName << " passed" << endl;
	else
		cout << testName << " FAILED" << endl;
}

int main() {
	// 底数、指数都为正数
	Test("Test1", 2, 3, 8, false);

	// 底数为负数、指数为正数
	Test("Test2", -2, 3, -8, false);

	// 指数为负数
	Test("Test3", 2, -3, 0.125, false);

	// 指数为0
	Test("Test4", 2, 0, 1, false);

	// 底数、指数都为0
	Test("Test5", 0, 0, 1, false);

	// 底数为0、指数为正数
	Test("Test6", 0, 4, 0, false);

	// 底数为0、指数为负数
	Test("Test7", 0, -4, 0, true);

	return 0;
}
```

**python代码：**

```python

```

