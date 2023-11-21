class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import defaultdict

        d = defaultdict(int)
        for item in arr:
            d[item] += 1

        num1 = len(d.keys())
        tmp = set()
        for val in d.values():
            tmp.add(val)
        num2 = len(tmp)
        return True if num1 == num2 else False