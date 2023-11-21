class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        used = [False]*10
        ans = []

        def comb(k, rem, tmp):
            if k == 0 and rem == 0:
                ans.append(tmp.copy())  # use copy to avoid referencing the same list
                return
            elif k == 0 or rem == 0:
                return

            for i in range(1 if not tmp else tmp[-1] + 1, 10):
                if not used[i] and rem >= i:
                    used[i] = True
                    tmp.append(i)

                    comb(k - 1, rem - i, tmp)

                    used[i] = False
                    tmp.pop()

        comb(k, n, [])
        return ans
