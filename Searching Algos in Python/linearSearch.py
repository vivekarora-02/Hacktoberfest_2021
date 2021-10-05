
def linearSearch(array, n, x):
 
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1
 
 
array = [2, 3, 4, 10, 40]
x = 5
n = len(array)
 
answer = linearSearch(array, n, x)
if(answer == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", answer)
