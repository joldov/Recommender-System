'''
@author: Jessica Oldov
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    d = {}
    """
    creating a dictionary and opening file given in getdata() to add data to 
    return it in the form of a two-tuple
    """
    f = open(filename)
    for each in f:
        data = each.strip().split(",")
        ratingslist = [x for x in data if data.index(x) % 2 == 0]
        if ratingslist[0] not in d:
            d[ratingslist[0]] = ratingslist[1:]
    lelist2 = [x for x in data if data.index(x) % 2 != 0]
    return (lelist2, d)

if __name__ == '__main__':
    getdata("data/books.txt")
