"""
Description: Check a word whether is a stop word or not.
Input: a str word, e.g. 'i'
Output: true or false, e.g. True
Author: Asirs Studio
"""


# a list of English stop words, refer to http://www.textfixer.com/tutorials/common-english-words.txt
stop_list = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among',
             'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but',
             'by', 'can', 'cannot', 'could', 'dear', 'did', 'do', 'does', 'either', 'else',
             'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he',
             'her', 'hers', 'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into',
             'is', 'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may', 'me',
             'might', 'most', 'must', 'my', 'neither', 'no', 'nor', 'not', 'of', 'off',
             'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say',
             'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their',
             'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas',
             'us', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while',
             'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your']


# check a word if in the stop word list
def is_stop_word(word):
    if word in stop_list:
        return True
    else:
        return False


# just for test
if __name__ == '__main__':
    sentence = ['i', 'like', 'information', 'retrieval', 'too']
    for word in sentence:
        if is_stop_word(word):
            sentence.remove(word)
    print(sentence)
