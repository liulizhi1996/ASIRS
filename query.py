"""
Description: Entry to search engineer.
Input: the directory of document set, the number of documents in it
Output: found results and their abstract, if any
Author: Asirs Studio
"""
from stemming import stem_for_str
from inverted_list import IndexList
from query_expansion import read_log, query_expansion
from read import read


# generate abstract for doc_id, and mark the word on pos_index
def abstract(dir_path, doc_id, pos_index):
    dir_name = (dir_path.partition('/'))[-1]
    file_path = dir_path + '/' + dir_name + str(doc_id) + '.txt'

    reader = open(file_path, 'r')
    doc = reader.readlines()
    reader.close()
    doc = ''.join(doc).split('\n')
    while '' in doc:
        doc.remove('')

    pos = 1
    for i in range(1, len(doc)):
        paragraph = doc[i]
        has_keyword = False
        output_paragraph = ''
        word_list = paragraph.split(sep=' ')
        for word in word_list:
            if pos in pos_index:
                output_paragraph += '*' + word + '* '
                has_keyword = True
            else:
                output_paragraph += word + ' '
            pos += 1
        if has_keyword:
            print('\t' + '...')
            print('\t' + output_paragraph)
    print()


# search for query, then output the results
def search(query, index_list, file_title_list, dir_path):
    dir_name = (dir_path.partition('/'))[-1]

    result = set()
    found = False
    pos_index = dict()
    for stem_keyword in query:
        if stem_keyword in index_list.index_list:
            inverted_list = set(index_list.index_list[stem_keyword].inverted_list)
            result |= inverted_list
            found = True
            for doc_id in inverted_list:
                if doc_id in pos_index:
                    pos_index[doc_id] |= set(index_list.index_list[stem_keyword].inverted_list[doc_id])
                else:
                    pos_index[doc_id] = set(index_list.index_list[stem_keyword].inverted_list[doc_id])
    if found:
        print('Find %d search results: ' % len(result))
        sorted(result)
        for doc_id in result:
            print(dir_name + str(doc_id) + ':', file_title_list[doc_id-1])
            abstract(dir_path, doc_id, pos_index[doc_id])
        print()
    else:
        print('No results.')
        print()


# main method for search engineer
def main(dir_path, doc_number):
    index_list = IndexList()
    file_title_list = list()
    read(dir_path, index_list, doc_number, file_title_list)

    while True:
        log_inverted_list = read_log('log.txt')

        query = input('Please input your query (Enter \'q\' to quit): ')
        if query == 'q':
            break
        query = query.lower()
        query = query.split(' ')
        query = [stem_for_str(keyword) for keyword in query]

        expansion_terms = query_expansion(index_list, query, doc_number, log_inverted_list)
        new_query = list(query)
        new_query.extend(expansion_terms)

        search(new_query, index_list, file_title_list, dir_path)
        clicked = input('Which one satisfies your need? Please enter here (spilt with \',\', \'?\' stands for none): ')
        print()

        log_writer = open('log.txt', 'a')
        for i in range(len(query)-1):
            log_writer.write(query[i] + ',')
        log_writer.write(query[len(query)-1])
        log_writer.write('\t' + clicked + '\n')
        log_writer.close()


# entry is here
if __name__ == '__main__':
    dir_path = 'datafile/cnn'
    doc_number = 20
    main(dir_path, doc_number)
