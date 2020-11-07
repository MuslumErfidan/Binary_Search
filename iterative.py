arr = [1, 3, 5, 7, 10] # Create a list
num = 10            # Select a number
def binary_search_ite(arr, first, last, num):
    mid = 0

    while first <= last:
        mid = (first + last)//2 # Searching for the middle off array 
        
        if arr[mid] < num: 
            first = mid + 1
        
        elif arr[mid] > num:
            last = mid - 1
            
        else:
            return mid
        
    return -1

final = binary_search_ite(arr, 0, len(arr)-1, num)
if final != -1:
    print("your number is at index", str(final))
    
else:
    print("your number is not included in your list")
