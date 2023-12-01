A = [1, 2, 2]
A = [4, 6, 4, 5, 6, 2]
A = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
n = len(A)
A_rev = A[::-1]

dp = [1]
for i in range(1, n):
    if A[i] > A[i-1]:
        dp.append(dp[-1] + 1)
    else:
        dp.append(1)

dp_rev = [1]
for i in range(1, n):
    if A_rev[i] > A_rev[i-1]:
        dp_rev.append(dp_rev[-1] + 1)
    else:
        dp_rev.append(1)
dp_rev = dp_rev[::-1]

for i in range(n):
    dp[i] = max(dp[i], dp_rev[i])

print(sum(dp))