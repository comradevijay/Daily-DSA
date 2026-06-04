# 26. Remove Duplicates from Sorted Array
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

def removeDub(nums):
    left = 0
    for right in range(1, len(nums)):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
    return left + 1

# print(removeDub([1,1,2]))   


