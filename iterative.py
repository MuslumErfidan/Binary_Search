arr = [1, 3, 5, 7, 10] # Create a list
num = 10            # Select a number
def binary_search_ite(arr, first, last, num): # Binary Search function
    mid = 0

    while first <= last: # While first element of array is less than or equal to the last element of array
        mid = (first + last)//2 # Searching for the middle of array 
        
        if arr[mid] < num: # Checking for the middle of array and variable(num)
            first = mid + 1 # Making the array half and remaking the first named variable
        
        elif arr[mid] > num: # Checking for the middle of array and variable(num)
            last = mid - 1 # Making the array half and remaking the last named variable
            
        else: # If middle of array is equal to our variable that named num
            return mid
        
    return -1 # If array is not sorted or empty 

final = binary_search_ite(arr, 0, len(arr)-1, num)
if final != -1: # If our function doesn't return -1 
    print("your number is at index", str(final))
    
else:
    print("your number is not included in your list")
