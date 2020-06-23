'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case: 1 or fewer characters remaining
    if len(word) <= 1:
        return 0

    # recursive cases
    # if the current leading letters are 'th' ->
    # return 1, skip two letters for the next pass
    if 'th' == word[:2]:
        return 1 + count_th(word[2:])
    # if the current first 2 letters are not 'th' ->
    # return 0, move to the next letter for the next pass
    else:
        return 0 + count_th(word[1:])
