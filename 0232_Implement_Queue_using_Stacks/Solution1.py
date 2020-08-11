class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.istk = []
        self.ostk = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.istk.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.ostk:
            i_size = len(self.istk)
            for _ in range(i_size):
                self.ostk.append(self.istk.pop())
        
        return self.ostk.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.ostk:
            i_size = len(self.istk)
            for _ in range(i_size):
                self.ostk.append(self.istk.pop())
        
        return self.ostk[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.istk == [] and self.ostk == []



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



def test1():
    que = MyQueue()
    que.push(1)
    que.push(2)
    res1 = que.peek()       # 1
    res2 = que.pop()        # 1
    res3 = que.empty()      # False
    if res1 == 1 and res2 == 1 and res3 == False:
        print('test1 success.')
    else:
        print('test1 failed.')

if __name__ == "__main__":
    test1()