class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        appeared_dict = defaultdict(list)

        for word in strs:
            counter = [0]*26
            for letter in word:
                counter[ord(letter)-97] += 1
            counter = tuple(counter)
            appeared_dict[counter].append(word)
            
            
        ans = []
        for val in appeared_dict.values():
            ans.append(val)
        return ans