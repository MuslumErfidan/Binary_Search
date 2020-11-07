arr = [1, 3, 5, 7, 10]
num = 7

def binary_search_rec(arr, first, last, num):
    if last >= first:
         mid = (first + last)//2
         
         if num == arr[mid]:
             return mid
         elif num < arr[mid]:
             return binary_search_rec(arr, first, mid-1, num)
         else:
             return binary_search_rec(arr, mid+1, last, num)
         
    else:
        return -1
    
final = binary_search_rec(arr, 0, len(arr)-1, num)

if final != -1:
    print("your number is at index",str (final))
    
else:
    print("your number is not included in your list")