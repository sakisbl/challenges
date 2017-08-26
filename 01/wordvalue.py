from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        content = f.readlines()
    return [x.strip() for x in content]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    result = 0
    for c in word:
        result += LETTER_SCORES.get(c.upper(), 0)
    return result

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words:
        return max(words, key=lambda w: calc_word_value(w))
    else:
        return max(load_words(), key=lambda w: calc_word_value(w))

if __name__ == "__main__":
    pass # run unittests to validate
