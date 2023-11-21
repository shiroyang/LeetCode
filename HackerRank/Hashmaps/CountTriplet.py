# Complete the countTriplets function below.
def countTriplets(arr, r):
    from collections import defaultdict
    # 逆から考える事によって順序を考える必要がなくなる
    pairs = defaultdict(int)
    triplets = defaultdict(int)
    ans = 0
    for item in reversed(arr):
        # 3つ揃った
        if item * r in triplets:
             ans += triplets[item*r]
        if item * r in pairs:
            triplets[item] += pairs[item*r]    
        pairs[item] += 1
    
    return ans
        

if __name__ == '__main__':
    _, r = map(int, input().split())
    arr = list(map(int, input().split()))
    print(countTriplets(arr, r))