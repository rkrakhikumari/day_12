def largest(arr, n):
    max = arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max = arr[i]
    return max

arr = [1,2,3,4,5,6]
n = len(arr)
ans = largest(arr, n)
print(f"largest no. in given array {ans}")


#### Using max()
def largest (arr, n):
    ans = max(arr)
    return ans
if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    n = len(arr)
    print(f"largest no. in the given array {largest(arr, n)}")


#### Using sort function
def largest(arr, n):
    arr.sort()
    return arr[-1]
arr = [1,2,6,5,3,7,2]
n = len(arr)
ans = largest(arr, n)
print(f"largest no. in given array is {ans}")


##### Using reducing function
from functools import reduce
def largest(arr):
    ans = reduce(max, arr)
    return ans
arr = [1,2,3,4,5,6]
n = len(arr)
ans = largest(arr)
print(f"largest in given array {ans}")


