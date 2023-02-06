# use list comperhension to return a list of all the words in a list 
# that has more than 4 characters

def more_char(li):

    return [s for s in li if len(s)>4]

