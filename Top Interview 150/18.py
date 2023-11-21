class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000, 500, 100, 50, 10, 5, 1]
        key = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        ans = ''

        first_digit = lambda x: int(str(x)[0])

        while num != 0:
            if first_digit(num) == 9:          
                if len(str(num)) == 3:
                    ans += 'CM'
                    num -= 900
                elif len(str(num)) ==2:
                    ans += 'XC'
                    num -= 90
                elif len(str(num)) == 1:
                    ans += 'IX'
                    num -= 9
                continue
            elif first_digit(num) == 4:
                if len(str(num)) == 3:
                    ans += 'CD'
                    num -= 400
                elif len(str(num)) ==2:
                    ans += 'XL'
                    num -= 40
                elif len(str(num)) == 1:
                    ans += 'IV'
                    num -= 4
                continue
            else:
                for i in range(len(val)):
                    rep = num // val[i]
                    if rep != 0:
                        num = num % val[i]
                        for _ in range(rep):
                            ans += key[i]
                        break
        
        return ans

