from ds.arrayList import ArrayList


class StringBuilder:
    def __init__(self):
        self.words = ArrayList(4)

    def append(self, word):
        self.words.insert(word)

    def toString(self):
        words = filter(lambda x: x is not None, self.words.getList())
        return " ".join(words)
