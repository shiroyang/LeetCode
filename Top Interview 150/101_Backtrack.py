class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        if not digits: return []
        ans = []
        def backtrack(res, cur):
            if len(res) == 0:
                ans.append(cur)
                return
            c = res[0]
            for letter in dic[c]:
                cur += letter
                backtrack(res[1:], cur)
                cur = cur[:-1]
        backtrack(digits, "")
        return ans