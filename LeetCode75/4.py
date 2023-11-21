from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:            
        def is_ok(x):
            if 0 < x < len(flowerbed)-1:
                if flowerbed[x-1] == 0 and flowerbed[x] == 0 and flowerbed[x+1] == 0:
                    return True
                else:
                    return False
            elif x == 0:
                if len(flowerbed) == 1:
                    return not flowerbed[0]
                if flowerbed[x] == 0 and flowerbed[x+1] == 0:
                    return True
                else:
                    return False
            elif x == len(flowerbed)-1:
                if flowerbed[x-1] == 0 and flowerbed[x] == 0:
                    return True
                else:
                    return False

        l = len(flowerbed)
        cnt = 0
        for i in range(l):
            if is_ok(i):
                flowerbed[i] = True
                cnt += 1
        
        return True if cnt >= n else False