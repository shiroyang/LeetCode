# Complete the freqQuery function below.
def freqQuery(queries):
    from collections import defaultdict
    
    d = defaultdict(int)
    freq = defaultdict(int)
    ans = []
    for idx, num in queries:
        if idx == 1:
            if d[num] > 0 and freq[d[num]] > 0:
                freq[d[num]] -= 1
            d[num] += 1
            freq[d[num]] += 1
        elif idx == 2:
            if d[num] > 0 and freq[d[num]] > 0:
                freq[d[num]] -= 1
            if d[num] > 0:
                d[num] -= 1
            if d[num] > 0:
                freq[d[num]] += 1
        elif idx == 3:
            ans.append(1 if freq[num]>0 else 0)
    
    return ans

if __name__ == '__main__':
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    ans = freqQuery(queries)
    print('\n'.join(map(str, ans)))
