"""
Description: Generate expansion terms.
Input: query terms, document terms
Output: the list of expansion terms
Author: Asirs Studio
"""
from tf_idf import normalized_weight
import math


# read log file in and return the inverted list of log
def read_log(log_path):
    log_inverted_list = dict()
    log_reader = open(log_path, 'r')
    for line in log_reader:
        log_line = line.rstrip('\n')
        log_line = log_line.split('\t')
        query = log_line[0].split(',')
        clicked_doc = log_line[1].split(',')
        if clicked_doc == ['?']:
            continue
        clicked_doc = [int(x) for x in clicked_doc]
        for word in query:
            for doc_id in clicked_doc:
                if word in log_inverted_list:
                    log_inverted_list[word].append(doc_id)
                else:
                    log_inverted_list[word] = [doc_id]

    return log_inverted_list


# compute f_{ik}^{(q)} (w_{i}^{(q)}, D_{k})
def frequency_word_clicked_doc(log_inverted_list, word, doc_id):
    if word in log_inverted_list:
        return log_inverted_list[word].count(doc_id)
    else:
        return 0


# compute f^{(q)} (w_{i}^{(q)})
def frequency_word(log_inverted_list, word):
    if word in log_inverted_list:
        return len(log_inverted_list[word])
    else:
        return 0


# compute P(w_{j}^{(d)} | w_{i}^{(q)})
def prob_doc_query(doc_word, query_word, doc_number, log_inverted_list, index_list):
    prob = 0
    for doc_id in range(1, doc_number+1):
        weight_vector = normalized_weight(index_list, doc_id, doc_number)
        maxs = -1
        for word in weight_vector:
            if weight_vector[word] > maxs:
                maxs = weight_vector[word]
        if doc_word in weight_vector:
            if query_word in log_inverted_list:
                prob += (weight_vector[doc_word] / maxs) * \
                        (frequency_word_clicked_doc(log_inverted_list, query_word, doc_id) /
                         frequency_word(log_inverted_list, query_word))
    return prob


# compute P(w_{j}^{(d)} | Q)
def query_expansion(index_list, query, doc_number, log_inverted_list):
    if log_inverted_list == {}:
        return []

    prob_list = dict()
    for doc_word in index_list.index_list:
        prod = 1
        for query_word in query:
            prod *= prob_doc_query(doc_word, query_word, doc_number, log_inverted_list, index_list) + 1
        prob_list[doc_word] = math.log10(prod)
    expansion_terms = sorted(prob_list.keys(), reverse=True)
    if len(expansion_terms) < 3:
        return expansion_terms
    else:
        return expansion_terms[:3]


# just for test
if __name__ == "__main__":
    log_inverted_list = read_log('log.txt')
    print(log_inverted_list)
    print(frequency_word_clicked_doc(log_inverted_list, 'salt', 1))
    print(frequency_word(log_inverted_list, 'salt'))
