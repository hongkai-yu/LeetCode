#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.LetterNode()

    class LetterNode:
        def __init__(self):
            self.children = [None] * 26  # list of WordNode
            self.isEndPoint = False

        def addLetterNode(self, letter: int) -> None:
            self.children[self._letterToIndex(letter)] = type(self)()

        def _letterToIndex(self, letter: str) -> int:
            return ord(letter) - 97

        def containsLetter(self, letter: int) -> bool:
            return self.getLetterNode(letter) is not None

        def getLetterNode(self, letter: int) -> 'LetterNode': # wait for python 3.10
            return self.children[self._letterToIndex(letter)]


    def _addWordNode(self, node: LetterNode, word: str) -> None:
        if word == '':
            node.isEndPoint = True
            return

        if not node.containsLetter(word[0]):
            node.addLetterNode(word[0])

        self._addWordNode(node.getLetterNode(word[0]), word[1:])

    def addWord(self, word: str) -> None:
        self._addWordNode(self.root, word)

    def _searchWordNode(self, node: LetterNode, word: str) -> bool:
        if word == '':
            return node.isEndPoint

        if word[0] == '.':
            for childNode in node.children:
                if childNode is not None and self._searchWordNode(childNode, word[1:]):
                    return True
            return False
        else:
            if not node.containsLetter(word[0]):
                return False
            else:
                return self._searchWordNode(node.getLetterNode(word[0]), word[1:])

    def search(self, word: str) -> bool:
        return self._searchWordNode(self.root, word)

    # Your WordDictionary object will be instantiated and called as such:
    # obj = WordDictionary()
    # obj.addWord(word)
    # param_2 = obj.search(word)
    # @lc code=end

if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord('hello')
    assert obj.search('hello')
    assert obj.search('h.llo')
    assert not obj.search('a.llo')
    assert not obj.search('h')

