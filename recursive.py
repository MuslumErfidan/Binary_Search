arr = [1, 3, 5, 7, 10] # Create a list
num = 7 # Select a number

def binary_search_rec(arr, first, last, num): # Binary Search function
    if last >= first: # While last element of array is more than or equal to the last element of array
         mid = (first + last)//2 # Searching for the middle of array 
         
         if num == arr[mid]: # If middle of array is equal to our variable that named num
             return mid 
         elif num < arr[mid]: # Checking for the middle of array and variable(num)
             return binary_search_rec(arr, first, mid-1, num) # Making the array half and remaking the variable that named last 
         else: # Checking for the middle of array and variable(num)
             return binary_search_rec(arr, mid+1, last, num) # Making the array half and remaking the variable that named first
         
    else: # While first element of array is less than the last element of array or if the array is not sorted and the if array is empty
        return -1
    
final = binary_search_rec(arr, 0, len(arr)-1, num)

if final != -1: # If our function doesn't return -1
    print("your number is at index",str (final))
    
else:
    print("your number is not included in your list")
