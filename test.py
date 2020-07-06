class Test:
    def f1(self):
        self.a += 1

    def f2(self):
        self.a = 0
        # self.f1()
        print('self.a = {}'.format(self.a))


if __name__ == '__main__':
    t = Test()
    # print('t.a = {}'.format(t.a))
    t.f2()
    print('t.a = {}'.format(t.a))