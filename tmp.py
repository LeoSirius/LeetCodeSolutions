a = '123456789'
b = '987654321'

res = 0
for i in iter(a):
		for j in iter(b):
				print('{} * {} = {}'.format(i, j, int(i) * int(j)))
				res += int(i) * int(j)

print(res)
