# Arrays

nums = [1, 2, 3]
sum(nums)
for n in nums:
    print(n)
    
nums.insert(1, 100) # insert 100 at index 1
print(nums)
nums.remove(100)
print(100 in nums)
print(nums)

# heap
import heapq

heapq.heapify(nums)

print(nums)