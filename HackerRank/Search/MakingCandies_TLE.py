# 極値が一つ存在するので、購入する回数を決める
m, w, p, n = map(int, input().split())

l = 0
r = 10**12

# x回の収益を全部投資に回し、n個以上のキャンディを作る時間を計算する
# mとwの差を減らすように投資する
memo = {} 

def calc(x):
    tmp_m = m; tmp_w = w
    days = x
    remainder = 0
    for i in range(x):
        if x in memo:
            tmp_m, tmp_w, remainder = memo[x]
            break
        # This is very tricky, you can not simply return days, because it may has optimal solution on the left
        if tmp_m * tmp_w > n: return days+100
        remainder += tmp_m * tmp_w
        num = remainder // p
        remainder %= p
        if tmp_m < tmp_w:
            first_transaction = min(num, tmp_w - tmp_m)
            tmp_m += first_transaction
            num -= first_transaction
            if num > 0:
                tmp_w += num // 2
                tmp_m += num - num // 2
        else:
            first_transaction = min(num, tmp_m - tmp_w)
            tmp_w += first_transaction
            num -= first_transaction
            if num > 0:
                tmp_m += num // 2
                tmp_w += num - num // 2
        memo[i+1] = [tmp_m, tmp_w, remainder]
        
        
    while remainder < n:
        remainder += tmp_m * tmp_w
        days += 1
    return days

# 三分探索
while r - l > 2:
    delta = (r-l) // 3
    mid1 = l + delta
    mid2 = r - delta
    
    if calc(mid1) < calc(mid2):
        r = mid2
    elif calc(mid1) > calc(mid2):
        l = mid1
    else:
        l = mid1
        r = mid2

print(min(calc(l), calc(l+1), calc(l+2), calc(r)))