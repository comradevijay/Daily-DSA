
#! 26. Remove Duplicates from Sorted Array
#? Input: nums = [1,1,2]
#? Output: 2, nums = [1,2,_]

def removeDub(nums):
    left = 0
    for right in range(1, len(nums)):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
    return left + 1

# print(removeDub([1,1,2]))   

#! 27. Remove Element
#? Input: nums = [3,2,2,3], val = 3
#? Output: 2, nums = [2,2,_,_]

def removeElement(nums, val):     
    l = 0
    for r in range(len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1
    return l

# print(removeElement([3, 2, 2, 3], 3))
