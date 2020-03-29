from collections import defaultdict
class WordNode:
    def __init__(self):
        self.children = collections.defaultdict(WordNode)
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = WordNode()


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        prev = self.root
        for s in word:
            prev = prev.children[s]
        prev.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        self.result = False
        self.dfs(node, word)
        return self.result


    def dfs(self, node: WordNode, word: str) -> None:
        if not word:
            if node.isEnd: self.result = True
            return
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node: return
            self.dfs(node, word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
