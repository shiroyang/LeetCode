class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # when row=3: 0->4->8->12  
        #             1->3->5->7
        #             2->6->8
        #
        # when row=4: 0->6->12
        #             1->5->7->11
        #             2->4->8->10
        #             3->9->15

        MOD = numRows*2-2
        n = len(s)
        if MOD == 0:
            return s
        ans = ['' for _ in range(numRows)]
        for i in range(n):
            if i % MOD < numRows:
                ans[i%MOD] += s[i]
            else:
                ans[MOD-i%MOD] += s[i]
        zigzag = ''
        for ls in ans:
            zigzag += ls
        return zigzag

