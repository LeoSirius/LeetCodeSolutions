import os

with open("test.sh", "r") as f:
    stream = f.read()
    # print(type(stream))
    upper_cnt = 0
    for ch in stream:
        if ch.isupper():
            upper_cnt += 1
    print("upper_cnt = {}".format(upper_cnt))

ls = [11,12,13,12,15,16,13]
ls = list(set(ls))
print("ls = {}".format(ls))

l1 = [1,5,7,9]
l2 = [2,2,6,8]
[1, 2, 2, 5, 6, 7, 9]
# res = [1,2,2,3,6,7,8,9]

p1, p2 = 0, 0
e1, e2 = len(l1) - 1, len(l2) - 1

res = []
while p1 != e1 and p2 != e2:
    if l1[p1] < l2[p2]:
        res.append(l1[p1])
        p1 += 1
    else:
        res.append(l2[p2])
        p2 += 1
    
if p1 != e1:
    res += l1[p1:]
if p2 != e2:
    res += l2[p2:]

print('res = {}'.format(res))

