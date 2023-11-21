class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        prefix = ""
        for c in searchWord:
            tmp = []
            prefix += c
            for idx, item in enumerate(products):
                if item.startswith(prefix):
                    tmp.append(item)
            ans.append(tmp[:3])
            products = tmp
        
        return ans