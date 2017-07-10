"""
Description: Implementation of positional index list. One word stores in positional index list as
    word1:
        [doc_id1: [pos1, pos2, pos3, ...];
         doc_id2: [pos1, pos2, pos3, ...];
         ...]
    word2:
        [doc_id1: [pos1, pos2, pos3, ...];
         doc_id2: [pos1, pos2, pos3, ...];
         ...]
    ...
Input: the word, document id and position index
Output: the positional index list
Author: Asirs Studio
"""


class InvertedList:
    """
    This class implements the inverted list using dict. For example:
        {'doc_id1': [pos1, pos2, ...], 'doc_id2': [pos1, pos2, ...], ...}
    """
    def __init__(self):
        self.inverted_list = dict()

    # insert into inverted list
    def add(self, doc_id, pos_index):
        if doc_id in self.inverted_list:
            self.inverted_list[doc_id].append(pos_index)
        else:
            self.inverted_list[doc_id] = [pos_index]

    # get the document frequent of this word
    def get_df(self):
        return len(self.inverted_list)

    # get the term frequent of this word in document doc_id
    def get_tf(self, doc_id):
        if doc_id in self.inverted_list:
            return len(self.inverted_list[doc_id])
        else:
            return 0

    # print out the whole list
    def print(self):
        for doc_id in self.inverted_list:
            print(str(doc_id) + ':', self.inverted_list[doc_id])


class IndexList:
    """
    Definition of positional index list using dict, like
        word1:
        [doc_id1: [pos1, pos2, pos3, ...];
         doc_id2: [pos1, pos2, pos3, ...];
         ...]
        word2:
            [doc_id1: [pos1, pos2, pos3, ...];
             doc_id2: [pos1, pos2, pos3, ...];
             ...]
        ...
    """
    def __init__(self):
        self.index_list = dict()

    # add new word to this list
    def add(self, word, doc_id, pos_index):
        if word in self.index_list:
            self.index_list[word].add(doc_id, pos_index)
        else:
            self.index_list[word] = InvertedList()
            self.index_list[word].add(doc_id, pos_index)

    # return document frequent of word
    def get_df(self, word):
        if word in self.index_list:
            return self.index_list[word].get_df()
        else:
            return 0

    # return term frequent of word in document doc_id
    def get_tf(self, word, doc_id):
        if word in self.index_list:
            return self.index_list[word].get_tf(doc_id)
        else:
            return 0

    # just print this list
    def print(self):
        for word in self.index_list:
            print(word + ':')
            self.index_list[word].print()
            print()


# just for test
if __name__ == '__main__':
    positional_index = IndexList()
    positional_index.add('angels', 2, 36)
    positional_index.add('angels', 2, 174)
    positional_index.add('angels', 2, 252)
    positional_index.add('angels', 2, 651)
    positional_index.add('angels', 4, 12)
    positional_index.add('angels', 4, 22)
    positional_index.add('angels', 4, 102)
    positional_index.add('angels', 4, 432)
    positional_index.add('angels', 7, 17)
    positional_index.add('fools', 2, 1)
    positional_index.add('fools', 2, 17)
    positional_index.add('fools', 4, 8)
    positional_index.add('fools', 7, 3)
    positional_index.add('fools', 7, 13)
    positional_index.add('fools', 7, 23)
    positional_index.print()
