def _sum(arr):
    sum =0
    for i in arr:
        sum = sum + i
    return(sum)
arr = [1,2,3,4,5,6]
ans = _sum(arr)
print(f"Sum of array is {ans}")


##### Using sum()
arr = [1,2,3,4,5,6]
ans = sum(arr)
print(f"Sum of array is {ans}")


#### Using reduce
from functools import reduce
def _sum(arr):
    sum = reduce(lambda a,b:a+b, arr)
    return sum
arr = [1,2,3,4,5,6]
ans = _sum(arr)
print(f"Sum of array is {ans}")


##### Using enumerate function
list1 = [1,2,3,4,5,6]
s = 0
for i, a in enumerate(list1):   
    s = s + a
print(s)


##### using counter
from collections import Counter
arr = [1,2,3,4,5,6]
c = Counter(arr)
sum = 0
for key, value in c.items():
    sum = sum + key * value
print(f"Sum of array is {sum}")
