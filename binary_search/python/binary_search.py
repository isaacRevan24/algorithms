def binary_search(input, item):
	low = 0
	high = len(input) - 1
	while low <= high:
		mid = (low+high)//2
		guess = input[mid]
		if guess > item:
			high = mid - 1
		elif guess < item:
			low = mid + 1
		else:
			return mid
	return None

input = [1, 3, 5, 6, 7, 9, 10]
item = 2

response = binary_search(input, item)
print(response)