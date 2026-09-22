class Trie(object):

    def __init__(self):
        self.root = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[None] = None
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr_node = self.root
        for char in word:
            if char not in curr_node:
                return False
            else:
                curr_node = curr_node[char]
        if None in curr_node:
            return True
        return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr_node = self.root
        for char in prefix:
            if char not in curr_node:
                return False
            else:
                curr_node = curr_node[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)