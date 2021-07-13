from collections import defaultdict


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msg2time = {}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if (message not in self.msg2time) or (timestamp - self.msg2time[message] >= 10):
            self.msg2time[message] = timestamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


def test1():
    logger = Logger()
    res1 = logger.shouldPrintMessage(1, 'foo')  # true
    res2 = logger.shouldPrintMessage(2, 'bar')  # true
    res3 = logger.shouldPrintMessage(3, 'foo')  # false
    res4 = logger.shouldPrintMessage(8, 'bar')  # false
    res5 = logger.shouldPrintMessage(10, 'foo') # false
    res6 = logger.shouldPrintMessage(11, 'foo') # true

    if (res1, res2, res3, res4, res5, res6) == (True, True, False, False, False, True):
        print('test1 succeed')
    else:
        print('test1 fail')


if __name__ == '__main__':
    test1()
