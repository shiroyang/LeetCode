a = [1,2,3]
m = 2

from bisect import bisect_left, insort_left
n = len(a)

def get_module(i,j):
    return (S[j] - S[i]) % m

S = [a[0]%m]
for item in a[1:]:
    S.append((S[-1] + item) % m)

ans = max(S)
sorted_set = [S[0]]

for i in range(1, n):
    idx = bisect_left(sorted_set, S[i])
    # アクセスできない
    if idx != len(sorted_set):
        ans = max(ans, (S[i] - sorted_set[idx] + m) % m)
    insort_left(sorted_set, S[i])
print(ans)