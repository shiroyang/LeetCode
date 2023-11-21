class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        # As long as you can swtich the letter, dont have to think about the order
        from collections import defaultdict

        d1 = defaultdict(int)
        d2 = defaultdict(int)
        counter1 = []
        counter2 = []
        ref1 = []
        ref2 = []
        for e in word1:
            d1[e] += 1

        for e in word2:
            d2[e] += 1
        
        for key, val in d1.items():
            ref1.append(key)
            counter1.append(val)
        for key, val in d2.items():
            ref2.append(key)
            counter2.append(val)
        ref1.sort()
        ref2.sort()
        counter1.sort()
        counter2.sort()

        if counter1 == counter2 and ref1 == ref2:
            return True
        else: return False

