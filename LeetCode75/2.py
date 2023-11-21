class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        l1 = len(str1); l2 = len(str2)
        l = min(len(str1), len(str2))
        for i in range(1, l+1):
            if l1 % i != 0 or l2 % i != 0: continue
            cnt1 = l1 // i; cnt2 = l2 // i
            tmp = str1[:i]
            is_ok = True
            for j1 in range(cnt1):
                for k in range(i):
                    if str1[j1*i+k] != tmp[k]:
                        is_ok = False
            for j2 in range(cnt2):
                for k in range(i):
                    if str2[j2*i+k] != tmp[k]:
                        is_ok = False
            
            if is_ok:
                ans = tmp


        return ans
    

A = Solution()
print(A.gcdOfStrings(str1 = "LEET", str2 = "CODE"))