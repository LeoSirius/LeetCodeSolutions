# kill.py

import os
import time
import signal

def create_child():
    pid = os.fork()
    if pid < 0:
        raise Exception
    return pid

pid = create_child()
if pid == 0:
    while True:    # 在子进程中循环打印
        print('in child process')
        time.sleep(1)

else:
    print('in parent process')
    time.sleep(5)                    # 父进程休眠5s再杀死子进程
    os.kill(pid, signal.SIGKILL)
    print(os.system('ps -ef|grep python'))
    time.sleep(5)                    # 父进程继续休眠5s观察子进程是否还有输出

