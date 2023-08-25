"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########




def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    
    new_paras = [para for para in paragraphs if select(para) == True]
    if k >= len(new_paras):
        return ''
    else:
        return new_paras[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def select(para):
        for item in topic:
            if item in split(lower(remove_punctuation(para))):
                return True
        else: return False
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    cnt, per = 0, 0.0
    for item_typed, item_refer in zip(typed_words, reference_words):
        if item_typed == item_refer:
            cnt += 1
    if len(typed_words) > 0:
        per = cnt/len(typed_words)*100
    
    return per
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    ela_min = elapsed/60
    return (len(typed)/5)/ela_min
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word
    else:
        # Initialization
        min_diff = diff_function(user_word, valid_words[0], limit)
        min_diff_index = 0
        # Find the min
        for index in range(1, len(valid_words)):
            diff = diff_function(user_word, valid_words[index], limit)
            if diff < min_diff:
                min_diff_index = index
                min_diff = diff

        if min_diff > limit:
            return user_word
        else:
            return valid_words[min_diff_index]

    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    if start == '' or goal == '':
        return abs(len(start) - len(goal))
    if start[0] == goal[0]:
        return shifty_shifts(start[1:], goal[1:], limit)
    else: 
        if limit == 0:
            return 1 # Minimize the computation to do so---Just add 1!
        return 1 + shifty_shifts(start[1:], goal[1:], limit - 1) # So smart!
    
    # END PROBLEM 6


def meowstake_matches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    

    if limit < 0: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END

    elif start == '' or goal == '': 
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(start) + len(goal)
        # END

    elif start[0] == goal[0]:
        return meowstake_matches(start[1:], goal[1:], limit)
    else:
        add_diff = meowstake_matches(start, goal[1:], limit - 1)
        remove_diff = meowstake_matches(start[1:], goal, limit - 1) 
        substitute_diff = meowstake_matches(start[1:], goal[1:], limit - 1) 
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 1 + min(add_diff, remove_diff, substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    i, index, flag = 0, 0, True
    while i < min(len(typed), len(prompt)):
        if typed[i] != prompt[i]:
            flag, index = False, i
            break
        i += 1
    if flag == True:
        index = len(typed)
    
    percentage = index/len(prompt)
    d = {'id': id, 'progress': percentage}
    send(d)
    return percentage
    
    # END PROBLEM 8



def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    
    for time in times_per_player:
        i = 0
        while i < len(time) - 1:
            time[i] = time[i + 1] - time[i]
            i += 1
        time.pop() # Delete the last member
        # Or: del(time[-1])
    return game(words, times_per_player)

    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    fastest = [[] for i in players]
    # fastest = []
    # for i in players:
    #     fastest.append([])
    for i in words:
        min_time_player = 0

        for j in players:
            if time(game, j, i) < time(game, min_time_player, i):
                min_time_player = j
        fastest[min_time_player] += [word_at(game, i)]

    return fastest
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = True  # Change to True when you

##########################
# Extra Credit #
##########################

key_distance = get_key_distances()
def key_distance_diff(start, goal, limit):
    """ 
    A diff function that takes into account the distances between keys when
    computing the difference score.
    Your task is to implement the function key_distance_diff. This is a diff function that, for every substitute operation where an existing letter is substituted with another letter, takes into account how far the letter being substituted in is from the letter being replaced. 
    For example, substituting "q" with "t" increases the difference measurement by twice as much as "q" and "e" because "q" and "t" are 4 keys apart, while "q" and "e" are 2 keys apart. 
    In the event where more than LIMIT number of changes need to be made, return the difference as infinite. Note that in python this can be done with float("inf").
    """

    start = start.lower() #converts the string to lowercase
    goal = goal.lower() #converts the string to lowercase

     # BEGIN PROBLEM EC1
    "*** YOUR CODE HERE ***"
    if limit < 0:
        return float('inf')
    if len(start) == 0 or len(goal) == 0:
        return len(start) + len(goal)
    elif start[0] == goal[0]:
        return key_distance_diff(start[1:], goal[1:], limit)
    else:
        add_diff = 1 + key_distance_diff(start, goal[1:], limit - 1)
        remove_diff = 1 + key_distance_diff(start[1:], goal, limit - 1) 
        kd = key_distance[(start[0], goal[0])]
        substitute_diff = kd + key_distance_diff(start[1:], goal[1:], limit - 1) 
        return min(add_diff, remove_diff, substitute_diff)
    # END PROBLEM EC1

def memo(f):
    """A memoization function as seen in John Denero's lecture on Growth"""

    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized

key_distance_diff = memo(key_distance_diff)
key_distance_diff = count(key_distance_diff)
memo_for_fa = {}


def faster_autocorrect(user_word, valid_words, diff_function, limit):
    """A memoized version of the autocorrect function implemented above."""

    # BEGIN PROBLEM EC2
    "*** YOUR CODE HERE ***"
    key = tuple([user_word, tuple(valid_words), diff_function, limit])
    if user_word in valid_words:
        return user_word
    if key in memo_for_fa:
        return memo_for_fa[key]
    else:
        # Initialization
        min_diff = diff_function(user_word, valid_words[0], limit)
        min_diff_index = 0
        # Find the min
        for index in range(1, len(valid_words)):
            diff = diff_function(user_word, valid_words[index], limit)
            if diff < min_diff:
                min_diff_index = index
                min_diff = diff

        if min_diff > limit:
            ret = user_word
        else:
            ret = valid_words[min_diff_index]
        memo_for_fa[key] = ret
        return ret
        # print("DEBUG: will is in the valid_words", "will" in valid_words)
        # print("DEBUG: dist(woll, will) = ", diff_function(user_word, "will", limit))
        # print("DEBUG: dist(woll, well) = ", diff_function(user_word, "well", limit))
        # words_diff = [diff_function(user_word, w, limit) for w in valid_words]
        # similar_word, similar_diff = min(zip(valid_words, words_diff), key=lambda item: item[1])
        # print("DEBUG:", similar_word)
        # if similar_diff > limit:
        #     ret = user_word
        # else:
        #     ret = similar_word
        # memo_for_fa[idx] = ret
        # return ret
    # END PROBLEM EC2


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)