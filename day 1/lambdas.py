"""def add5(val):
    return val+5

print(add5(100))



alist=['learn','python','step']
output=list(map(lambda x:x.upper(),alist))
print(type(output))
print(output)

#single line functions are called lambda functions
add5=lambda x : x+5
print(type(add5))
print(add5(100))
sm=lambda x:True if x.startswith('M') else False
print(sm('murthy'))"""

#filter
'''scores=[66,90,68,59,76,60,80]
#def is_A_student(score):
#    return score>75
checker=lambda x: x>75
over_75= list(filter(checker, scores))
print(over_75)'''

#sort
'''list1=[("eggs",5.25),("honey",9.5),("carrots",1.4)]
list1.sort(key=lambda x:x[0],reverse=0)
#True-1 False-0
print(list1)'''


#numpy

import numpy as np
x=np.array([2,4,6,8])
squarer = lambda t:t**2
squares = np.array ([squarer(xi) for xi in x])
print(squares)

