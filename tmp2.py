from functools import cmp_to_key

nums = ['30', '3']

def cmp(a, b):
    print('a = {}, b = {}, b+a = {}, a+b = {}'.format(a, b, b+a, a+b))
    return int(b+a) - int(a+b)

if __name__ == "__main__":
    nums.sort(key=cmp_to_key(cmp))
    print(nums)