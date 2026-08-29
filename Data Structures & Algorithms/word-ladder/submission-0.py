class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        Q = deque()
        Q.append((beginWord,1))
        s = set(wordList)
        
        if beginWord in s:
            s.remove(beginWord)

        while Q:
            word,steps = Q.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                originalChar = word[i]
                for ch in range(ord('a'),ord('z')+1):
                    newChar = chr(ch)
                    if newChar != originalChar:
                        newWord = word[:i]+newChar+word[i+1:]
                        
                        if newWord in s:
                            s.remove(newWord)
                            Q.append((newWord,steps+1))
                
                
        return 0