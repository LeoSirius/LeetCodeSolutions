class CQueue:

    def __init__(self):
        self.istk = []
        self.ostk = []


    def appendTail(self, value: int) -> None:
        self.istk.append(value)


    def deleteHead(self) -> int:
        if not self.ostk:
            if not self.istk:
                return -1
            while self.istk:
                self.ostk.append(self.istk.pop())
        return self.ostk.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()


def test1():
    q = CQueue();
    q.appendTail(3);
    res1 = q.deleteHead();
    res2 = q.deleteHead();

    if (res1, res2) == (3, -1):
        print('test1 success.')
    else:
        print('test1 failed.')

if __name__ == '__main__':
    test1()
