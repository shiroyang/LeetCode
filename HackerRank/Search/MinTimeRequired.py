def is_ok(x, goal):
    tmp = 0
    for item in A:
        tmp += x // item
    return tmp >= goal

n, goal = map(int, input().split())
A = list(map(int, input().split()))

l = 1
r = 10**32

while r - l > 1:
    mid = (l + r) // 2
    if is_ok(mid, goal):
        r = mid
    else:
        l = mid
print(r)