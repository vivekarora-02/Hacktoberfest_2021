def binarySearch (array, l, r, x):
  
    if r >= l:
  
        mid = l + (r - l) 
  
        # If element is present at the middle itself
        if array[mid] == x:
            return mid
          

        elif array[mid] > x:
            return binarySearch(array, l, mid-1, x)
  
       
        else:
            return binarySearch(array, mid + 1, r, x)
  
    else:
     
        return -1
  
array = [ 2, 3, 4, 10, 40 ]
x = 5
  
answer = binarySearch(array, 0, len(array)-1, x)
  
if answer != -1:
    print ("Element is present at index % d" % answer)
else:
    print ("Element is not present in array")
