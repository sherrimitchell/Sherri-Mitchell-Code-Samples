# iterating two monotonic pointers across an array to search for a pair of indices satisfying some condition in linear time
# the two-pointer method iterates two pointers across an array, to track start and end of an interval. can be used to track two values in an array
# find the longest contiguous array of books that can be read within t minutes
# define left and right to represent beginning and end of a segment. both start at the beginning of the array. these 2 numbers represent pointers.
# for every value of left in increasing order, increase right until the total time for the segment is maximized while being <= t.
# ans will store the maximum value of right - left + 1 (segment size) that we have encountered so far.
# after incrementing left by 1, the time used decreases, hence the right pointer never has to move leftwards.
# one-indexed integer array: arr[1] ... arr[n]
# Q different pairs - (a, b) - a + b
# prefix sum is also known as a partial sum
# prefix sum array - prefix[0] = 0
# 1 <= k <= n. k = len(prefix), n = len(arr)
# element at index k of prefix sum array stores the sum of all the elements from the original array from index 1 up to k
# prefix[k]= prefix[k-1] + arr[k]

# nums = [1,0,-1,0,-2,2]
# nums = [7, 6, 4, -1, 1, 2]
# arr = [1, 6, 4, 2, 5, 3]
# prefix = [0, 1, 7, 11, 13, 18, 21]
# N = 6
books = [3, 1, 2, 1]
# number of minutes
t = 4
n = len(books)
right = 0
left = 0
cur = 0
ans = 0

while left < n and right < n:
    # find the max right for which cur < t
    while right < n:
        # add book to current total. increment the right pointer.
        cur += books[right]
        right += 1
        # if the current total > t, decrement the right pointer, subtract the previous book from the current total.
        #
        if cur > t:
            right -= 1
            cur -= books[right]
            break
        print("current:", cur)
    # check the max number of books. subtract the previous book from the current total. move the left pointer.
    ans = max(ans, right - left)
    cur -= books[left]
    left += 1

    print(ans)