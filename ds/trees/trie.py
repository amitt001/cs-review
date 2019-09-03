"""Trie implementation"""


class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        node = self.root
        for w in key:
            index = self._char_to_index(w)
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end = True

    def search(self, key):
        node = self.root
        for w in key:
            index = self._char_to_index(w)
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node and node.is_end




if __name__ == '__main__':
    trie = Trie()
    trie.insert('amit')
    trie.insert('name')
    trie.insert('named')
    assert trie.search('named') is True
    assert trie.search('nam') is False
