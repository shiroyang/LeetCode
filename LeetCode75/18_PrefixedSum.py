class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        Accum = [0]
        ma = 0
        for item in gain:
            tmp = Accum[-1]+item
            Accum.append(tmp)
            if tmp > ma:
                ma = tmp

        return ma
            
