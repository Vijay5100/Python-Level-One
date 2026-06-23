ages = [10,12,13,14,15]
# print(max(ages))
# print(min(ages))
# print(sum(ages))
# print(sum(ages)/len(ages))
# range(start,stop,step)
"""
start -> optional , default is 0 
step -> optional , default is 1 


step -> how much you need add to the current number to 
get the next number 
stop -> where to stop 
"""
# for i in range(len(ages)):# 0 to n-1 
#     print(ages[i])
# print(list(range(1,10)))
for i in range(len(ages)):
    print(ages[i])
numbers = list(range(1,101))
print(len(numbers))  

n = int(input("Enter number of items you want to add: "))
values = [] # length = 0 
for i in range(n):
    number = (input("Enter a name: "))
    values.append(number) # add the element at the end of the list 
print(values)
    
