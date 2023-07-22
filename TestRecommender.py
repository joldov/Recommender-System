'''
@author: Jessica Oldov
'''

import SmallDukeEatsReader
import RecommenderEngine


def driver():
    (items,ratings) = SmallDukeEatsReader.getdata()
    print("items = ",items)
    print("ratings = ", ratings)
    
    avg = RecommenderEngine.averages(items,ratings)
    #print("average",avg)
    if avg == [('DivinityCafe', 4.0), ('TheCommons', 3.0),
               ('Tandoor', 2.4285714285714284), ('IlForno', 1.8),
               ('FarmStead', 1.4), ('LoopPizzaGrill', 1.0), ('TheSkillet', 0.0),
               ('PandaExpress', -0.2),
               ('McDonalds', -0.3333333333333333)]:
        print("averages work")
    else:
        print("averages fails")

    similarities = RecommenderEngine.similarities("Sung-Hoon", ratings)
    if similarities == [('Wei', 1), ('Sly one', -1), ('Melanie', -2),
                        ('Sarah Lee', -6), ('J J', -14), ('Harry', -24),
                        ('Nana Grace', -29)]:
        print("similarities work")
    else:
        print("similarities fails")

    recommendations = RecommenderEngine.recommendations("Sarah Lee",
                                                        ["DivinityCafe",
                                                         "FarmStead", "IlForno",
                                                         "LoopPizzaGrill",
                                                         "McDonalds",
                                                         "PandaExpress",
                                                         "Tandoor",
                                                         "TheCommons",
                                                         "TheSkillet"], {
                                                            "Sarah Lee": [3, 3,
                                                                          3, 3,
                                                                          0, -3,
                                                                          5, 0,
                                                                          -3],
                                                            "Melanie":
                                                                [5, 0, 3, 0, 1,
                                                                 3, 3, 3, 1],
                                                            "J J": [0, 1, 0, -1,
                                                                    1, 1, 3, 0,
                                                                    1],
                                                            "Sly one": [5, 0, 1,
                                                                        3, 0, 0,
                                                                        3, 3,
                                                                        3],
                                                            "Sung-Hoon": [0, -1,
                                                                          -1, 5,
                                                                          1, 3,
                                                                          -3, 1,
                                                                          -3],
                                                            "Nana Grace": [5, 0,
                                                                           3,
                                                                           -5,
                                                                           -1,
                                                                           0, 1,
                                                                           3,
                                                                           0],
                                                            "Harry":
                                                                [5, 3, 0, -1,
                                                                 -3, -5, 0, 5,
                                                                 1],
                                                            "Wei": [1, 1, 0, 3,
                                                                    -1, 0, 5, 3,
                                                                    0]}, 3)

    if recommendations == [('Tandoor', 149.5), ('TheCommons', 128.0),
                           ('DivinityCafe', 123.33333333333333),
                           ('FarmStead', 69.5),
                           ('TheSkillet', 66.0), ('LoopPizzaGrill', 62.0),
                           ('IlForno', 33.0), ('McDonalds', -69.5),
                           ('PandaExpress', -165.0)]:
        print("recommendations work")
    else:
        print("recommendations fails")

    # for key in ratings:
    #     slist = RecommenderEngine.similarities(key,ratings)
    #     print(key,slist)
    #     r3 = RecommenderEngine.recommendations(key,items,ratings,3)
    #     print("top",r3)
        
        
        
if __name__ == '__main__':
    driver()