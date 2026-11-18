class Trie:

    def __init__(self):
        self.children = {}
        self.is_word = False
        

    def insert(self, word: str) -> None:
        curr_trie = self
        for char in word:
            if char not in curr_trie.children:
                curr_trie.children[char] = Trie()
            curr_trie = curr_trie.children[char]
        curr_trie.is_word = True

    def search(self, word: str) -> bool:
        curr_trie = self
        for char in word:
            if char not in curr_trie.children:
                return False
            curr_trie = curr_trie.children[char]
        return curr_trie.is_word

    def startsWith(self, prefix: str) -> bool:
        curr_trie = self
        for char in prefix:
            if char not in curr_trie.children:
                return False
            curr_trie = curr_trie.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)