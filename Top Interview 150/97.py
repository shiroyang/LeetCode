class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        BFS to explore the word combinations. 
        At each step, try changing each character of the current word and 
        see if it results in a word from the wordList.    
        """
        from collections import deque
        wordSet = set(wordList)

        n = len(beginWord)
        if endWord not in wordSet: return 0
        
        que = deque()
        que.append((beginWord, 1))
        
        while que:
            word, step = que.popleft()

            if word == endWord:
                return step
            for i in range(n):
                for j in range(26):
                    new = word[:i] + chr(97+j) + word[i+1:]
                    if new in wordSet:
                        que.append((new, step+1))
                        wordSet.remove(new)
        return 0