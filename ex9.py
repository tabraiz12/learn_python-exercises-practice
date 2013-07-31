def break_words(stuff):
    """This function will break up words for us."""

    #this is .split
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    # this is sorted 
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    # pop words
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    # pop last word
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    # call break_words func
    words = break_words(sentence)
    # call sort_word
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    # call break_words func
    words = break_words(sentence)

    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)