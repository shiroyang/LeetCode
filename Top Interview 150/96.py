class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque
        if startGene == endGene: return 0
        used = {startGene}
        def calc_diff(ls1, ls2):
            cnt = 0
            for i in range(min(len(ls1), len(ls2))):
                if ls1[i] != ls2[i]:
                    cnt += 1
            return cnt

        cur = startGene
        que = deque()
        for i in range(len(bank)):
            if calc_diff(cur, bank[i]) == 1:
                que.append((bank[i], 1))
        
        while que:
            cur, step = que.popleft()
            used.add(cur)
            if cur == endGene:
                return step
            for i in range(len(bank)):
                if calc_diff(cur, bank[i]) == 1 and bank[i] not in used:
                    que.append((bank[i], step+1))
        
        return -1