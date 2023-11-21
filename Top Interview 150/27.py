class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l_idx = 0
        r_idx = n-1

        while l_idx < r_idx:
            tmp = numbers[l_idx] + numbers[r_idx]
            if tmp == target:
                return [l_idx+1, r_idx+1]
            elif tmp > target:
                r_idx -= 1
            else:
                l_idx += 1