"""
Description: Compute tf-idf.
Input: positional index, document id, number of documents
Output: a dict called document vector, like
    {word1: tf-idf1, word2: tf-idf2, ...}
Author: Asirs Studio
"""
from inverted_list import IndexList
import math


# compute idf_{i}^{(d)}
def idf(word, doc_number, index_list):
    return math.log10(doc_number / (1 + index_list.get_df(word)))


# compute W_{i}^{(d)} without normalization
def weight(word, doc_id, word_number, doc_number, index_list):
    return math.log10(1 + index_list.get_tf(word, doc_id) / word_number) * idf(word, doc_number, index_list)


# normalization
def normalize(weight_list):
    sums = sum([weight_list[x] * weight_list[x] for x in weight_list])
    for x in weight_list:
        weight_list[x] /= math.sqrt(sums)
    return weight_list


# compute normalized weight vector
def normalized_weight(index_list, doc_id, doc_number):
    word_list = []
    for word in index_list.index_list:
        if doc_id in index_list.index_list[word].inverted_list:
            word_list.append(word)
    weight_vector = dict()
    for word in word_list:
        weight_vector[word] = weight(word, doc_id, doc_number, len(word_list), index_list)
    weight_vector = normalize(weight_vector)
    return weight_vector


# just for test
if __name__ == '__main__':
    positional_index = IndexList()
    positional_index.add('this', 1, 36)
    positional_index.add('is', 1, 174)
    positional_index.add('a', 1, 252)
    positional_index.add('a', 1, 289)
    positional_index.add('sample', 1, 12)
    positional_index.add('this', 2, 22)
    positional_index.add('is', 2, 102)
    positional_index.add('another', 2, 432)
    positional_index.add('another', 2, 17)
    positional_index.add('example', 2, 1)
    positional_index.add('example', 2, 17)
    positional_index.add('example', 2, 34)

    weight_vector = normalized_weight(positional_index, 1, 2)
    print(weight_vector)
