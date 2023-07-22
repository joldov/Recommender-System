'''
@author: Jessica Oldov
'''
import operator
def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    answer = []
    for x in range(len(items)):
        item = items[x]
        count = 0
        sum = 0
        """
        return the second element which is a float (even the zero)
        """
        for y in ratings.values():
            if y[x] != 0:
                sum += y[x]
                count +=1
        if count > 0:
            equal = (item, float((sum)/count))
        else:
            equal = (item, float(0))
        answer.append(equal)
        """
        here we are sorting our answer 
        """
        fin = sorted(answer, key=operator.itemgetter(1), reverse=True)
    return fin


def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    answer = []

    for key in ratings:
        if name == key:
            originalcompare = ratings[key]

    for key in ratings:
        if name == key:
            continue
        if name != key:
            sum = 0
            for num in range(len(ratings[key])):
                product = ratings[key][num] * originalcompare[num]
                sum += product
        answer.append((key, sum))
    """
    here we are sorting our answer and breaking ties alphabetically
    """
    #final = sorted(answer, key=operator.itemgetter(1), reverse=True)
    alpha_sort = sorted(answer, key=operator.itemgetter(0), reverse=False)
    final = sorted(alpha_sort, key=operator.itemgetter(1), reverse=True)
    return final

def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''
    d = {}
    """
    calling similarities()
    """
    weightavgs = similarities(name, ratings)
    for x in range(numUsers):
        tup = weightavgs[x]
        person = tup[0]
        multiplier = tup[1]
        leorig = ratings[person]
        list1 = [multiplier * num for num in leorig]
        if person not in d:
            d[person] = list1
    """
    calling averages()
    """
    answer = averages(items, d)
    """
    here we are sorting our answer and sorting the second value in reverse 
    order
    """
    final = sorted(answer, key=operator.itemgetter(0))
    final = sorted(final, key=operator.itemgetter(1), reverse=True)
    return final

if __name__ == '__main__':
    recommendations("Sarah Lee",["DivinityCafe", "FarmStead", "IlForno","LoopPizzaGrill","McDonalds", "PandaExpress","Tandoor", "TheCommons", "TheSkillet"],{"Sarah Lee": [3, 3, 3, 3, 0, -3, 5, 0, -3], "Melanie":[5, 0, 3, 0, 1, 3, 3, 3, 1],"J J": [0, 1, 0, -1, 1, 1, 3, 0, 1],"Sly one": [5, 0, 1, 3, 0, 0, 3, 3, 3],"Sung-Hoon": [0, -1, -1, 5, 1, 3, -3, 1, -3],"Nana Grace": [5, 0, 3, -5, -1, 0, 1, 3, 0], "Harry":[5, 3, 0, -1, -3, -5, 0, 5, 1],"Wei": [1, 1, 0, 3, -1, 0, 5, 3, 0]}, 3)
