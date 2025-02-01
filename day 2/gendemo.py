from logdemo import logger

def square_numbers(nums):
    for i  in nums:
        yield(i*i)   #no resturn as we are returning generator

my_nums=square_numbers([1,2,3,4,5])
print(type(my_nums))
#print(next(my_nums))
#print(next(my_nums))
for i in my_nums:
    print(i)