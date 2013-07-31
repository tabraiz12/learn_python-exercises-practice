# import random library
import random
# import urlopen from urllib
from urllib import urlopen
# import sys lib
import sys

# assign url to word_url
WORD_URL = "http://learncodethehardway.org/words.txt"
# create a Words List
WORDS = []
# create a dict named phrases
PHRASES = {
    "class ###(###):":
      "Make a class named ### that is-a ###.",
    "class ###(object):\n\tdef __init__(self, ***)" :
      "class ### has-a __init__ that takes self and *** parameters.",
    "class ###(object):\n\tdef ***(self, @@@)":
      "class ### has-a function named *** that takes self and @@@ parameters.",
    "*** = ###()":
      "Set *** to an instance of class ###.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

print PHRASES
# do they want to drill phrases first

PHRASE_FIRST = False

# check the length of args
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up the words from the website
# open url using urlopen and readline
for word in urlopen(WORD_URL).readlines():
    # append url to words
    print word
    WORDS.append(word.strip())

# function convert
def convert(snippet, phrase):
    
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("###"))]
    print class_names
    other_names = random.sample(WORDS, snippet.count("***"))
    print other_names
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    print param_names
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("###", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"