#iterator design paatern

data=[10,20,30,40]
#print(data[2])
#for i in data:
#    print(i)  #iterator
'''
d=iter(data)
print(type(d))
print(d.__next__())
print(d.__next__())
print(next(d))
print(next(d))
'''

#pandas.head(100)
#pandas.tail(100)
#custom iterator
class Head:
    def __init__(self,size=5):
        self.num=1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num<=5:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
        
values=Head(100)
'''print(values.__next__())#1
print(values.__next__())#2
print(values.__next__())#3
print(values.__next__())#4
print(values.__next__())#5'''

for i in values:
    print(i)
