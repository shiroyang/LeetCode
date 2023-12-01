# dp[i][j]: prev i, j is selected or not, max sum
_  = input()
A = list(map(int, input().split()))

n = len(A)
ans = 0
dp = [[0] * 2 for _ in range(n + 1)]

for i in range(n):
    dp[i+1][0] = max(dp[i][0], dp[i][1])
    dp[i+1][1] = max(dp[i-1][0] + A[i], dp[i-1][1] + A[i])
    
print(max(dp[-1]))