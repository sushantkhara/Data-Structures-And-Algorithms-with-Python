def binary_search(arr, beg, end, item):
	if end >= beg:
		mid = (beg + end)//2
		if arr[mid] == item:
			return mid+1
		elif arr[mid]< item:
			return binary_search(arr, mid+1, end, item)
		elif arr[mid] > item:
			return binary_search(arr, mid-1, beg, item)
	else:
		return -1


arr = []
n = int(input("Enter size of the array: \n"))
print("Enter the elements : \n")
for i in range(0, n): 
    ele = int(input()) 
    arr.append(ele)

arr =sorted(arr)
print(arr)
item  = int(input("Enter item you want to search: \n"))	
loc = -1
loc = binary_search(arr, 0, n, item)
if loc != -1:
    print("Item found at location %d" %loc)
else:
    print("Item not found")