### 思路1

用一个queue和一个deque实现

保值deque的首部一直是最大的值

queue就是正常的que，负责push和pop

deque用来存放最大值
如果新的value大于deque尾端的值，那么deque一直进行pop_back操作，
直到尾端的值大于等于value 或者为空

再将value压入deque的尾部
每次取max_value，返回deque首部的值。

即deq是从头到尾递减的，deq.front()即是最大值

当que进行pop操作时，如果que首部的值等于deque首部的值，那么deque同样需要进行pop_front操作

===============

注意这道题和min stack，不能直接用一个栈来保存最大值。

一个错误的实例：

如入队顺序

4 3 2 1

栈里只有4

当que pop4之后，栈就空了，这显然是错误的
