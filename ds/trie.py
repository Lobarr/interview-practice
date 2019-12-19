from typing import Dict


class TrieNode:
  def __init__(self, char = ''):
    self.children: Dict[str, TrieNode] = {}
    self.char: str = char
    self.isWord: bool = False

  def setIsWord(self, isWord: bool):
    self.isWord = isWord

  def hasChild(self, char: str):
    return char in self.children

  def setChild(self, char: str, node):
    self.children[char] = node

SPECIAL_NODE = TrieNode('SPECIAL_NODE')

class Trie:
  def __init__(self):
    self.root: TrieNode = SPECIAL_NODE

  def insert(self, word):
    cur = self.root
    for char in word:
      childNode = None
      if not cur.hasChild(char):
        print('creating new char node')
        childNode = TrieNode(char)
        cur.setChild(char, childNode)
        cur = childNode
      else:
        cur = cur.children[char]
    cur.setIsWord(True)
    print('set new word')

  def search(self, word: str):
    cur: TrieNode = self.root
    for char in word:
      if not char in cur.children:
        return False
      cur = cur.children[char]
    return True if cur.isWord else False
      
if __name__ == '__main__':
  trie = Trie()
  for word in ['testing', 'something','this','should','work']:
    trie.insert(word)
  
  for testCase in [('testing', True), ('false', False), ('work', True), ('word', False)]:
    assert trie.search(testCase[0]) == testCase[1]



