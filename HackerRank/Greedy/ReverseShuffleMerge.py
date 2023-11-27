s = input()
char_cnt = {}
used_cnt = {}
ans = []
for e in s: char_cnt[e] = char_cnt.get(e, 0) + 1
remaining_cnt = {k: v for k, v in char_cnt.items()}
def can_be_used(c):
    return used_cnt.get(c, 0) < char_cnt[c] // 2

# 最後の文字を捨てても構わない
def can_be_popped(c):
    return used_cnt.get(c, 0) - 1 + remaining_cnt[c] >= char_cnt[c] // 2
    
for c in reversed(s):
    if can_be_used(c):
        while ans and ans[-1] > c and can_be_popped(ans[-1]):
            removed = ans.pop()
            used_cnt[removed] -= 1
        ans.append(c)
        used_cnt[c] = used_cnt.get(c, 0) + 1
    remaining_cnt[c] -= 1
print(''.join(ans))