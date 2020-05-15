"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

"""
import collections
class root:
    def __init__(self):
        self.children = collections.defaultdict(root)
        self.word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=root()
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        location=self.root
        for i in word:
            location=location.children[i]
        location.word=True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        location=self.root
        for i in word:
            location=location.children.get(i)
            if location is None:
                return False
        return location.word
    
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        location=self.root
        for i in prefix:
            location=location.children.get(i)
            if location is None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
