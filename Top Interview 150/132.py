class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ptr = len(digits)-1
        digits[ptr] += 1
        while ptr:
            if digits[ptr] < 10:
                return digits
            else:
                digits[ptr] -= 10
                digits[ptr-1] += 1
            ptr -= 1
            
        if digits[0] > 9:
            digits[0] -= 10
            digits = [1] + digits[:]
        return digits