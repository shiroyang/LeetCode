class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur:        
                cur[letter] = {}
            cur = cur[letter]
        cur['*'] = True

    def search(self, word: str) -> bool:
        
        def search_in_node(word, cur) -> bool:
            if not word:
                return '*' in cur
            letter = word[0]

            if letter in cur or letter == '.':
                if letter == '.':
                    for key in cur:
                        if key != '*' and search_in_node(word[1:], cur[key]):
                            return True
                else:
                    return search_in_node(word[1:], cur[letter])       
            else: return False

        return search_in_node(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)