'''
@author: Jessica Oldov
'''


def getdata(filename):
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    d = {}
    lelist = []
    """
    opening a file to read it and return it in the form of a two-tuple
    """
    f = open(filename)
    for line in f:
        data = line.strip().split(",")
        movie = data[1]

        lelist.append(movie)
        lelist = sorted(set(lelist))
    f.close()

    f2 = open(filename)
    for line in f2:
        zeros = [0 for x in range(len(lelist))]
        data2 = line.strip().split(",")
        id = data2[0]
        movie2 = data2[1]
        rate = int(data2[2])

        if id not in d:
            d[id] = zeros

        dex = lelist.index(movie2)
        d[id][dex] = rate

    return (lelist, d)


if __name__ == '__main__':
    getdata("data/movies.txt")
