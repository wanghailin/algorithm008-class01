class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        N = len(beginWord)
        visited = {beginWord: True}
        wordMap = defaultdict(list)
        for word in wordList:
            for i in range(N):
                wordMap[word[:i] + '*' + word[i+1:]].append(word)
        queue = [(beginWord, 1)]
        while queue:
            currentWord, level = queue.pop(0)
            for i in range(N):
                wordKey = currentWord[:i] + '*' + currentWord[i+1:]
                for word in wordMap[wordKey]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level +1))
        return 0