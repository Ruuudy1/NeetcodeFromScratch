class TrieNode:
    def __init__(self):
        #the tree is just a hashmap
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        # we only need a root node 
        # to get the first character in the word
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root # start at the root

        # check each character to see if its already in the trie
        for c in word: 
            if c not in cur.children:
                #if no child from the root create one
                cur.children[c] = TrieNode()
            # if it is then move our pointer there and keep iterating
            cur = cur.children[c]
        cur.endOfWord = True 
        #once the word ends we assign the last character 
        # the endOfWord indicator

    def search(self, word: str) -> bool:
#####################Walk through Trie############################
        cur = self.root

        for c in word:        
            if c not in cur.children:
                return False
            cur = cur.children[c] 
##################################################################
        return cur.endOfWord #return true if it is the end of the word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True # none of the prev characters were 
                    # False so it does start with c