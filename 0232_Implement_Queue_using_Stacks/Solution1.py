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
        if len(self.ostk) == 0:
            while len(self.istk):
                self.ostk.append(self.istk.pop())
        return self.ostk.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.ostk) == 0:
            while len(self.istk):
                self.ostk.append(self.istk.pop())
        return self.ostk[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.istk) == len(self.ostk) == 0


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
