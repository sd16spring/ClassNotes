"""
Find mirror pairs of words from a word list.

Mirror pairs exist when a valid word can be formed both forward and backward
e.g. tuba <-> abut

Palindromes are a special case of mirror pairs, and mirror pairs can be
useful in constructing palindromic phrases.
"""

def reverse_word(word):
    """
    Return a string with characters in 'word' reversed.

    >>> reverse_word("software")
    'erawtfos'
    """
    backwards_word = ""
    for i in range(len(word)):
        backwards_word += word[len(word)-1-i]
    return backwards_word


def has_mirror_pair(word, all_words):
    """
    Given a 'word' to check and a full set of 'all_words',
    return True if 'word' has a mirror pair within 'all_words'.
    """    
    for candidate in all_words:
        if reverse_word(word) == candidate:
            return True
    return False

def find_mirror_pairs(word_list, max_search=-1):
    """
    Return a list of all words in 'word_list' that have a mirror
    pair within the word_list.

    If 'max_search' is given, only look for mirror pairs for the 
    first 'max_search' words; otherwise search full 'word_list'.
    """

    # BUG: For some reason this doesn't search the whole word_list
    #      if I don't provide max_search - figure it out later.
    pairs = []
    for word in word_list[:max_search]:
        if has_mirror_pair(word, word_list):
            pairs.append(word)
    return pairs


def get_wordlist(filename):
    """
    Return a list of words from 'filename', which must be a word
    list text file with one word per line.
    """
    words = []
    with open(filename, "r") as fp:
        for line in fp:
            words.append(line.strip())
    return words


# Run if called from the command line
if __name__ == "__main__":
    words = get_wordlist("words.txt")
    print find_mirror_pairs(words, 100)
