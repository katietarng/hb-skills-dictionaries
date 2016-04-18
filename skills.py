"""Skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different::

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    no_duplicates = set(words)
    no_duplicates = list(no_duplicates)

    return no_duplicates


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    common_items = set(items1) & set(items2)
    common_items = list(common_items)

    return common_items


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    word_count = {}

    words = phrase.split()

    for word in words: 
        if word in word_count: 
            word_count[word] += 1
        else: 
            word_count[word] = 1    

    return word_count


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    #List of keys
    english = ['man','hotel','student',
               'boy','professor','restaurant',
               'your', 'excuse','student', 
               'are','restroom', 'my',
               'is'
               ]

    #List of values
    pirate = ['matey', 'fleabag inn', 'swabbie',
              'matey', 'foul blaggart', 'galley', 
              'yer', 'arr', 'swabbie', 
              'be', 'head', 'me', 
              'be'
              ]


    translation = dict(zip(english,pirate)) #create key,pair values by mapping list indices
    
    words = phrase.split()
    pirate_phrase = translation[words[0]]
    words = words[1:]

    for word in words: 

        if word in translation: 
            pirate_phrase += ' ' + translation[word]
        else: 
            pirate_phrase += ' ' + word  
    
    return pirate_phrase


def sort_by_word_length(words):
    """Given list of words, return list of ascending (len, [words]).

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- the length
    of the words for that word-length, and the list of words of
    that word length.

    For example::

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]
    """

    word_length = []

    for i in range(len(words)):

        length = (len(words[i]), [words[i]])

        if length in word_length: 
            pass
        else: 
            word_length.append(length)

        for j in range(1, len(word_length)): 

            if i + j < len(words):

                if len(words[i + j]) == len(words[i]):
                    #If the length at word index [i] = to the length at word index [i+j], add the word
                    word_length.append(words[i + j])
                else:
                    pass 

    sorted_word_length = sorted(word_length)
    return sorted_word_length

    #Able to append words but unable to append a word onto an existing length


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    pairs = []

    for i in range(len(numbers)): 
        #If number at any index is 0, append the number in the list
        if numbers[i] == 0:
            pairs.append((numbers[i],0))

        #Iterate through numbers after the current index[i]
        for j in range(i+1, len(numbers)): 

            #If the sum of number at index[i] and index[j] = 0, add the pair as a tuple to the list
            if numbers[i] + numbers[j] == 0: 
                pair = (numbers[i], numbers[j])
                pairs.append(pair)
 
    no_duplicate_pairs = set(pairs)

    #Unable to get rid of pairs that are the reverse of each other (1,-1) and (-1,1) 
    pairs = list(no_duplicate_pairs)
    pairs = sorted(pairs)    

    return pairs


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    word_chain = [] 

    first_word = names[0]
    word_chain.append(first_word)

    words = {}
  
    #Create dictionary of words mapped to the word's first letter
    for i in range(len(names)):
        
        letter = names[i][0]

        words[letter] = words.get(letter, [])

        if names[i][0] == letter:
            words[letter].append(names[i])

    for i in range(len(names)):
        #Take last letter of first word to find next word 

        key = tuple(words.keys())

        #If the last letter at word_chain[index] is in the keys of the words dictionary
        #Append the first word in the values list for that key
        if word_chain[i][-1] in key: 
            key = word_chain[i][-1]

            first_word_value = words[key][0]

            #If word is already in the word chain and the length of the value list at that key is more than 1
            if first_word_value in word_chain and len(words[key]) > 1:
                next_word = words[key][1]
                word_chain.append(next_word)
            else:
                word_chain.append(first_word_value)

            #Seeing 'yamask', 'kalob', and 'baltoy' pop up again 
        i = i+1  

    return word_chain


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
