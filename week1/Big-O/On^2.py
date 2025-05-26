# Traversing a square grid

# nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(nums)):
#     print("\n", nums[i])
#     print(i)
#     for j in range(len(nums[i])):
#         # print("\n", nums[j])
#         # print(j)
#         print(nums[i][j])
        
# for row in nums:
#     for num in row:
#         print("\n", num)
        
nums = [1, 2, 3]
for i in range(len(nums)): # i iterates over the indices [0, 1, 2]
    # print(i) # provide the index
    # print(nums[i]) # provides the values in the array
    for j in range(i + 1, len(nums)): # j iterates from (i + 1) to len(nums)
        # print(i, j) 
        print(nums[i], nums[j]) # Prints the value at index i, j
        