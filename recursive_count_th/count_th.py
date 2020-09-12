'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) == 0:
        return 0

    # look for th at the beginning of the word
    if word[0:2] == 'th':
        # if we found th, call this function again removing the th we found
        return 1 + count_th(word[2:])
    else:
        # if we did not find th, just remove the first letter and call this function again
        return count_th(word[1:])
