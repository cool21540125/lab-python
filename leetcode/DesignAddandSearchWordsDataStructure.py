import re


class WordDictionary:
    def __init__(self):
        self.words = []

    def addWord(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        if word in self.words:
            return True

        if "." not in word:
            return False

        for idx in range(len(self.words)):
            _current_word = self.words[idx]
            if len(word) != len(_current_word):
                continue
            qq = re.match(rf"{word}", _current_word, flags=re.S)
            if qq:
                return True

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
