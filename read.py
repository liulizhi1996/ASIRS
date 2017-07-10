"""
Description: Read the document set and generate our positional index list and title list.
Input: the directory of document set, the number of documents in it
Output: the positional index list, title list
Author: Asirs Studio
"""
from stemming import stem_for_str
from stop_list import is_stop_word
from inverted_list import IndexList


# pre-process the word
def process(word):
    returned_word = word

    # check if it's made up of the symbols
    is_useless = True
    for ch in word:
        if ch not in {'~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=',
                      '{', '[', '}', ']', '\\', '|', ':', ';', '\'', '\"', '<', ',', '>', '.', '?', '/'}:
            is_useless = False
            break
    if is_useless:
        return ''

    # discard the first and last symbol, if any
    if word[0] in {'~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=',
                   '{', '[', '}', ']', '\\', '|', ':', ';', '\'', '\"', '<', ',', '>', '.', '?', '/'}:
        returned_word = word[1:]
    if word[-1] in {'~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=',
                    '{', '[', '}', ']', '\\', '|', ':', ';', '\'', '\"', '<', ',', '>', '.', '?', '/'}:
        returned_word = word[:-1]

    # convert into lower case
    returned_word = returned_word.lower()

    # stem
    returned_word = stem_for_str(returned_word)

    return returned_word


# process one document
def read_doc(dir_path, index_list, doc_id, file_title_list):
    dir_name = (dir_path.partition('/'))[-1]
    file_path = dir_path + '/' + dir_name + str(doc_id) + '.txt'

    reader = open(file_path, 'r')
    doc = reader.readlines()
    reader.close()

    doc = ''.join(doc).split('\n')
    while '' in doc:
        doc.remove('')

    file_title_list.append(doc[0])

    pos = 1
    for i in range(1, len(doc)):
        paragraph = doc[i]
        word_list = paragraph.split(sep=' ')
        for word in word_list:
            word = process(word)
            if word != '' and not is_stop_word(word):
                index_list.add(word, doc_id, pos)
            pos += 1


# process the whole document set
def read(dir_path, index_list, doc_number, file_title_list):
    for doc_id in range(1, doc_number+1):
        read_doc(dir_path, index_list, doc_id, file_title_list)


# just for test
if __name__ == "__main__":
    dir_path = 'datafile/NBA'
    index_list = IndexList()
    file_title_list = list()
    read(dir_path, index_list, 20, file_title_list)
    print(file_title_list)
    index_list.print()
