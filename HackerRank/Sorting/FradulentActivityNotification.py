from bisect import bisect_left
def get_median(cnt, d):
    S = [0]
    for i in range(201):
        S.append(S[-1] + cnt[i])
    S = S[1:]
    if d%2 == 1:
        return bisect_left(S, d//2+1)
    else:
        m1 = bisect_left(S, d//2)
        m2 = bisect_left(S, d//2+1)
        return (m1+m2)/2

n, d = map(int, input().split())
expenditure = list(map(int, input().split()))
ans = 0
cnt = [0]*201

for i in range(d):
    cnt[expenditure[i]] += 1
    
for j in range(d, n):
    if expenditure[j] >= 2*get_median(cnt, d):
        ans += 1
    cnt[expenditure[j-d]] -= 1
    cnt[expenditure[j]] += 1
      
print(ans)