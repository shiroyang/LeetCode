class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2letter = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        ans = []
        if len(digits) == 0:
            return []
        def backtrack(digits, s):
            if len(digits) == 0:
                ans.append(s)
                return 
            tmp = digits[0]
            digits = digits[1:]

            for letter in num2letter[tmp]:
                backtrack(digits, s+letter)
        
        backtrack(digits, "")

        return ans