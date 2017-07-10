"""
Description: Stem a word using the porter's stemming algorithm.
Input: a str word, e.g. 'interesting'
Output: a str word after stemming, e.g. 'interest'
Author: Asirs Studio
"""


# The function vc_num returns the measure of any word or word part.
# Any word, or part of a word, has the following form :
#          m
#  [C] (VC) [V]
#   where C is a series of consonant and
#         V is a series of vowel.
# Hence, the function returns the number of repetition of VC in the word, or the part of a word.
def vc_num(word, i):
    vcnum = 0
    consonant = 1
    for k in range(i+1):
        if word[k] not in {'a', 'e', 'i', 'o', 'u'}:
            if word[k] == 'y':
                if k == 0:
                    flag = 1
                else:
                    if consonant == 1:
                        flag = 0
                    else:
                        flag = 1
            else:
                flag = 1
        else:
            flag = 0
        if flag == 1:
            if consonant == 0:
                vcnum += 1
        consonant = flag
    return vcnum


# The function determines if the stem contains a vowel.
def vowel(word, i):
    consonant = 0
    for k in range(i+1):
        if word[k] not in {'a', 'e', 'i', 'o', 'u'}:
            if word[k] == 'y':
                if consonant == 1:
                    return 1
            consonant = 1
        else:
            return 1
    return 0


# The function determines if the stem ends with a double consonant.
def double_letter(word, i):
    if i >= 1:
        if word[i] == word[i-1]:
            if word[i] not in {'a', 'e', 'i', 'o', 'u', 'y'}:
                return 1
    return 0


# The function checks if the stem end with cvc, where the second c is not w, x or y.
def end_cvc(word, i):
    if i >= 2:
        if word[i] not in {'a', 'e', 'i', 'o', 'u', 'y', 'w', 'x'}:
            if word[i-1] in {'a', 'e', 'i', 'o', 'u', 'y'}:
                if word[i-2] not in {'a', 'e', 'i', 'o', 'u'}:
                    if word[i-2] == 'y':
                        consonant = 0
                        for j in range(i-2):
                            if word[j] not in {'a', 'e', 'i', 'o', 'u'}:
                                if word[j] == 'y':
                                    if consonant == 1:
                                        consonant = 0
                                    else:
                                        consonant = 1
                                else:
                                    consonant = 1
                            else:
                                consonant = 0
                        if consonant == 0:
                            return 1
                    else:
                        return 1
    return 0


# This function takes in a word key and returns the stem form of word using the same pointer key.
# It implements the 5 major steps of the Porter's algorithm.
def stem(word):
    i = len(word) - 1
    ret_value = i

    # Step 1 a
    if i >= 0 and word[i] == 's':
        if i >= 1:
            if word[i-1] == 'e':
                if i >= 2 and word[i-2] == 'i':
                    word[i-1] = word[i] = '\0'
                    i -= 2
                else:
                    if i >= 3 and word[i-2] == 's' and word[i-3] == 's':
                        word[i] = word[i-1] = '\0'
                        i -= 2
                    else:
                        word[i] = '\0'
                        i -= 1
            elif word[i-1] == 's':
                pass
            else:
                word[i] = '\0'
                i -= 1
        else:
            word[i] = '\0'
            i -= 1

    # Step 1 b
    if i >= 1:
        flag = 0
        if word[i] == 'd' and word[i-1] == 'e':
            if i >= 2 and word[i-2] == 'e':
                if vc_num(word, i-3) > 0:
                    word[i] = '\0'
                    i -= 1
            else:
                if vowel(word, i-2) == 1:
                    word[i] = word[i-1] = '\0'
                    i -= 2
                    flag = 1
        else:
            if i >= 2 and word[i] == 'g' and word[i-1] == 'n' and word[i-2] == 'i':
                if vowel(word, i-3) == 1:
                    word[i] = word[i-1] = word[i-2] = '\0'
                    i -= 3
                    flag = 1
        if flag == 1:
            if i >= 1:
                if (word[i-1] == 'a' and word[i] == 't') or \
                    (word[i-1] == 'b' and word[i] == 'l') or \
                        (word[i-1] == i and word[i] == 'z'):
                    i += 1
                    word[i] = 'e'
                else:
                    if double_letter(word, i) == 1 and word[i] not in {'l', 's', 'z'}:
                        word[i] = '\0'
                        i -= 1
                    else:
                        if vc_num(word, i) == 1 and end_cvc(word, i) == 1:
                            i += 1
                            word[i] = 'e'

    # Step 1 c
    if word[i] == 'y':
        if vowel(word, i-1) == 1:
            word[i] = 'i'

    # Step 2
    if i >= 1:
        if word[i-1] == 'a':
            if word[i] == 'l':
                if i >= 5 and word[i-2] == 'n' and word[i-3] == 'o' and \
                                word[i-4] == 'i' and word[i-5] == 't':
                    if i >= 6 and word[i-6] == 'a':
                        if vc_num(word, i-7):
                            word[i] = word[i-1] = word[i-2] = word[i-3] = '\0'
                            word[i-4] = 'e'
                            i -= 4
                    else:
                        if vc_num(word, i-6) > 0:
                            word[i] = word[i-1] = '\0'
                            i -= 2
        elif word[i-1] == 'c':
            if word[i] == 'i':
                if i >= 3 and word[i-2] == 'n' and word[i-3] in {'a', 'e'}:
                    if vc_num(word, i-4) > 0:
                        word[i] = 'e'
        elif word[i-1] == 'e':
            if word[i] == 'r':
                if i >= 3 and word[i-2] == 'z' and word[i-3] == 'i':
                    if vc_num(word, i-4) > 0:
                        word[i] = '\0'
                        i -= 1
        elif word[i-1] == 'l':
            if word[i] == 'i':
                if i >= 2 and word[i-2] == 'e':
                    if vc_num(word, i-3) > 0:
                        word[i] = word[i-1] = '\0'
                        i -= 2
                else:
                    if i >= 3 and word[i-2] == 'b' and word[i-3] == 'a':
                        if vc_num(word, i-4) > 0:
                            word[i] = 'e'
                    else:
                        if i >= 3 and word[i-2] == 'l' and word[i-3] == 'a':
                            if vc_num(word, i-4) > 0:
                                word[i] = word[i-1] = '\0'
                                i -= 2
                        else:
                            if i >= 4 and (
                                    (word[i-2] == 't' and word[i-3] == 'n' and word[i-4] == 'e') or
                                    (word[i-2] == 's' and word[i-3] == 'u' and word[i-4] == 'o')):
                                if vc_num(word, i-5) > 0:
                                    word[i] = word[i-1] = '\0'
                                    i -= 2
        elif word[i-1] == 'o':
            if word[i] == 'n':
                if i >= 4 and word[i-2] == 'i' and word[i-3] == 't' and word[i-4] == 'a':
                    if i >= 6 and word[i-5] == 'z' and word[i-6] == 'i':
                        if vc_num(word, i-7) > 0:
                            word[i] = word[i-1] = word[i-2] = word[i-3] = '\0'
                            i -= 4
                            word[i] = 'e'
                    else:
                        if vc_num(word, i-5) > 0:
                            word[i] = word[i-1] = '\0'
                            i -= 2
                            word[i] = 'e'
            elif word[i] == 'r':
                if i >= 3 and word[i-2] == 't' and word[i-3] == 'a':
                    if vc_num(word, i-4) > 0:
                        word[i] = '\0'
                        i -= 1
                        word[i] = 'e'
        elif word[i-1] == 's':
            if word[i] == 's':
                if i >= 6 and word[i-2] == 'e' and word[i-3] == 'n' and (
                        (word[i-4] == 'e' and word[i-5] == 'v' and word[i-6] == 'i') or
                        (word[i-4] == 'l' and word[i-5] == 'u' and word[i-6] == 'f') or
                        (word[i-4] == 's' and word[i-5] == 'u' and word[i-6] == 'o')):
                    if vc_num(word, i-7) > 0:
                        word[i] = word[i-1] = word[i-2] = word[i-3] = '\0'
                        i -= 4
            elif word[i] == 'm':
                if i >= 4 and word[i-2] == 'i' and word[i-3] == 'l' and word[i-4] == 'a':
                    if vc_num(word, i-5) > 0:
                        word[i] = word[i-1] = word[i-2] = '\0'
                        i -= 3
        elif word[i-1] == 't':
            if word[i] == 'i':
                if i >= 2 and word[i-2] == 'i':
                    if i >= 3:
                        if word[i-3] == 'l':
                            if i >= 4:
                                if word[i-4] == 'a':
                                    if vc_num(word, i-5) > 0:
                                        word[i] = word[i-1] = word[i-2] = '\0'
                                        i -= 3
                                elif word[i-4] == 'i':
                                    if i >= 5 and word[i-5] == 'b':
                                        if vc_num(word, i-6) > 0:
                                            word[i] = word[i-1] = word[i-2] = '\0'
                                            i -= 3
                                            word[i] = 'e'
                                            word[i-1] = 'l'
                        elif word[i-3] == 'v':
                            if i >= 4 and word[i-4] == 'i':
                                if vc_num(word, i-5) > 0:
                                    word[i] = word[i-1] = '\0'
                                    i -= 2
                                    word[i] = 'e'

    # Step 3
    if i >= 0:
        if word[i] == 'e':
            if i >= 4:
                if (word[i-1] == 't' and word[i-2] == 'a' and word[i-3] == 'c' and word[i-4] == 'i') or \
                        (word[i-1] == 'z' and word[i-2] == 'i' and word[i-3] == 'l' and word[i-4] == 'a'):
                    if vc_num(word, i-5) > 0:
                        word[i] = word[i-1] = word[i-2] = '\0'
                        i -= 3
                else:
                    if word[i-1] == 'v' and word[i-2] == 'i' and word[i-3] == 't' and word[i-4] == 'a':
                        if vc_num(word, i-5) > 0:
                            word[i] = word[i-1] = word[i-2] = word[i-3] = word[i-4] = '\0'
                            i -= 5
        elif word[i] == 'i':
            if i >= 4:
                if word[i-1] == 't' and word[i-2] == 'i' and word[i-3] == 'c' and word[i-4] == 'i':
                    if vc_num(word, i-5) > 0:
                        word[i] = word[i-1] = word[i-2] = '\0'
                        i -= 3
        elif word[i] == 'l':
            if i >= 1:
                if word[i-1] == 'a':
                    if i >= 3:
                        if word[i-2] == 'c' and word[i-3] == 'i':
                            if vc_num(word, i-4) > 0:
                                word[i] = word[i-1] = '\0'
                                i -= 2
                if word[i-1] == 'u':
                    if i >= 2:
                        if word[i-2] == 'f':
                            if vc_num(word, i-3) > 0:
                                word[i] = word[i-1] = word[i-2] = '\0'
                                i -= 3
        elif word[i] == 's':
            if i >= 3:
                if word[i-1] == 's' and word[i-2] == 'e' and word[i-3] == 'n':
                    if vc_num(word, i-4) > 0:
                        word[i] = word[i-1] = word[i-2] = word[i-3] = '\0'
                        i -= 4

    # Step 4
    if i >= 1:
        if word[i-1] == 'a':
            if word[i] == 'l':
                if vc_num(word, i-2) > 1:
                    word[i] = word[i-1] = '\0'
                    i -= 2
        elif word[i-1] == 'c':
            if word[i] == 'e':
                if i >= 3:
                    if word[i-2] == 'n' and (word[i-3] == 'a' or word[i-3] == 'e'):
                        if vc_num(word, i-4) > 1:
                            word[i] = word[i-1] = word[i-2] = word[i-3] = '\0'
                            i -= 4
        elif word[i-1] == 'e':
            if word[i] == 'r':
                if vc_num(word, i-2) > 1:
                    word[i] = word[i-1] = '\0'
                    i -= 2
        elif word[i-1] == 'i':
            if word[i] == 'c':
                if vc_num(word, i-2) > 1:
                    word[i] = word[i-1] = '\0'
                    i -= 2
        elif word[i-1] == 'l':
            if word[i] == 'e':
                if i >= 3:
                    if word[i-2] == 'b' and word[i-3] in {'a', 'i'}:
                        if vc_num(word, i-4) > 1:
                            word[i] = word[i-1] = word[i-2] = word[i-3] = '\0'
                            i -= 4
        elif word[i-1] == 'n':
            if word[i] == 't':
                if i >= 2:
                    if word[i-2] == 'a':
                        if vc_num(word, i-3) > 1:
                            word[i] = word[i-1] = word[i-2] = '\0'
                            i -= 3
                    elif word[i-2] == 'e':
                        if i >= 3 and word[i-3] == 'm':
                            if i >= 4 and word[i-4] == 'e':
                                if vc_num(word, i-5) > 1:
                                    word[i] = word[i-1] = word[i-2] = word[i-3] = word[i-4] = '\0'
                                    i -= 5
                            else:
                                if vc_num(word, i-4) > 1:
                                    word[i] = word[i-1] = word[i-2] = word[i-3] = '\0'
                                    i -= 4
                        else:
                            word[i] = word[i-1] = word[i-2] = '\0'
                            i -= 3
        elif word[i-1] == 'o':
            if word[i] == 'u':
                if vc_num(word, i-2) > 1:
                    word[i] = word[i-1] = '\0'
                    i -= 2
            else:
                if i >= 2 and word[i] == 'n' and word[i-2] == 'i':
                    if word[i-3] in {'s', 't'} and vc_num(word, i-3) > 1:
                        word[i] = word[i-1] = word[i-2] = '\0'
                        i -= 3
        elif word[i-1] == 's':
            if i >= 2 and word[i] == 'm' and word[i-2] == 'i':
                if vc_num(word, i-3) > 1:
                    word[i] = word[i-1] = word[i-2] = '\0'
                    i -= 3
        elif word[i-1] == 't':
            if i >= 2 and ((word[i] == 'e' and word[i-2] == 'a') or (word[i] == 'i' and word[i-2] == 'i')):
                if vc_num(word, i-3) > 1:
                    word[i] = word[i-1] = word[i-2] = '\0'
                    i -= 3
        elif word[i-1] == 'u':
            if i >= 2 and word[i-2] == 'o' and word[i-1] == 'u' and word[i] == 's':
                if vc_num(word, i-3) > 1:
                    word[i] = word[i-1] = word[i-2] = '\0'
                    i -= 3
        elif word[i-1] == 'v':
            if i >= 2 and word[i] == 'e' and word[i-2] == 'i':
                if vc_num(word, i-3) > 1:
                    word[i] = word[i-1] = word[i-2] = '\0'
                    i -= 3
        elif word[i-1] == 'z':
            if i >= 2 and word[i] == 'e' and word[i-2] == 'i':
                if vc_num(word, i-3) > 1:
                    word[i] = word[i-1] = word[i-2] = '\0'
                    i -= 3

    # Step 5 a
    if i >= 0:
        if word[i] == 'e':
            if vc_num(word, i-1) > 1 or (vc_num(word, i-1) == 1 and end_cvc(word, i-1) == 0):
                word[i] = '\0'
                i -= 1

    # Step 5 b
    if vc_num(word, i) > 1 and double_letter(word, i) == 1 and word[i] == 'l':
        word[i] = '\0'
        i -= 1

    return ret_value > i


# Main method here, stem for str word.
def stem_for_str(word):
    list_word = list(word)
    stem(list_word)
    while '\0' in list_word:
        list_word.remove('\0')
    return ''.join(list_word)


# just for test
if __name__ == '__main__':
    test_word = 'interesting'
    stem_word = stem_for_str(test_word)
    print(stem_word)
