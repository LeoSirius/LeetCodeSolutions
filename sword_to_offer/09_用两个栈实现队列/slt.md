### 思路1

stack1做队尾，stack2做队头。栈是先进后出，队列是先进先出。我们只要把栈的顺序倒一下，就变成队列的顺序了。具体做法是：

1. appendTail，直接push到stack1中
2. deleteHead，若stack2空，把stack1中的所有元素弹出亚入到stack2中，再从内stack2中删除。如果stack2还不空。则直接弹出stack2中元素。
