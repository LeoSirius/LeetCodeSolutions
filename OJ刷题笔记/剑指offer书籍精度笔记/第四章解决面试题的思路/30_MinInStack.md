**思路：**

```
为了保留栈的特性，不改变原来的数据栈，而是新加一个辅助站来保存最小元素。
```



**c\c++代码：**

```c++
#pragma once

#include<stack>
#include<assert.h>

template<typename T> class StackWithMin {
public:
	StackWithMin() {}
	virtual ~StackWithMin() {}

	T& top();
	const T& top() const;

	void push(const T& value);
	void pop();

	const T& min() const;

	bool empty() const;
	size_t size() const;

private:
	std::stack<T> m_data;
	std::stack<T> m_min;
};

template<typename T> 
void StackWithMin<T>::push(const T& value) {
	m_data.push(value);

    // 当新元素比之前的最小元素小时，把新元素插入辅助栈里；
    // 否则把之前的最小元素重复插入辅助栈里
	if (m_min.size() == 0 || value < m_min.top())
		m_min.push(value);
	else
		m_min.push(m_min.top());
}

template<typename T>
void StackWithMin<T>::pop() {
	assert(m_data.size() > 0 && m_min.size() > 0);
	m_data().pop();
	m_min().pop();
}

template<typename T> 
const T& StackWithMin<T>:min() const {
	assert(m_data.size() > 0 && m_min.size() > 0);
	return m_min.top();
}

template<typename T>
T& StackWithMin<T>::top() {
	return m_data.top();
}

template<typename T>
const T& StackWithMin<T>::top() const {
	return m_data.top();
}

template<typename T>
bool StackWithMin<T>::empty() const {
	return m_data.empty();
}

template<typename T>
szie_t StackWithMin<T>::size() const {
	return m_data.size();
}
```

**python代码：**

```python

```

