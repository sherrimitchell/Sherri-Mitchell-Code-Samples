# nums = [1]
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [5, 4, -1, 7, 8]
nums = [-2, -1]

maxSum = float('-inf')
currentSum = 0
currentElement = 0

for x in nums:
	currentElement = max(0, x)
	currentSum = max(0, currentSum + x)
	maxSum = max(maxSum, currentSum)
	print("currentSum and maxSum: ", currentSum, maxSum)
	print("maxSum: ", maxSum)

	if currentSum == 0:
		currentSum = maxElement

	print("max element: ", maxElement)
# return maxSum



# maxSum = 0
# currentSum = 0
# for x in nums:
# 	currentSum = max(0, currentSum + x)

	
# 	if len(nums) < 2:
# 		# return x
# 		print("x: ", x)
   
		
# 		maxSum = max(maxSum, currentSum)
# 	print("maxSum: ", maxSum)

# return maxSum

# for (int i = 0; i < size; i++)
# {
#     max_ending_here = max(max_ending_here + array[i], 0);
#     max_so_far      = max(max_ending_here, max_so_far);
#     max_element     = max(max_element, array[i]);
# }

# if (max_so_far == 0)
#   max_so_far = max_element;

# printf("%d\n", max_so_far);