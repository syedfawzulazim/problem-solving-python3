class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currLevel = self.root
        for ch in word:
            if ch not in currLevel.children.keys():
                currLevel.children[ch] = TrieNode()
        
            currLevel = currLevel.children[ch]
             
        currLevel.isEndOfWord = True

    def search(self, word: str) -> bool:
        currLevel = self.root
        for ch in word:
            if not ch in currLevel.children:
                return False
            currLevel = currLevel.children[ch]
        if currLevel and  currLevel.isEndOfWord:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        currLevel = self.root
        for ch in prefix:
            if not ch in currLevel.children:
                return False
            currLevel = currLevel.children[ch]                                      
        return True
    
obj = Trie()
obj.insert("app")
obj.insert("apps")
print(obj.search("app"))
print(obj.search("apps"))

# print(obj.startsWith("app"))
