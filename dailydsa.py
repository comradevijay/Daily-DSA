
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


#! 349. Intersection of Two Arrays

def arrayIntersection(nums1, nums2):
    arr = []
    nums1 = set(nums1)
    nums2 = set(nums2)
    for i in nums1:
        if i in nums2 and i not in arr:
            arr.append(i)   
    return arr   

# print(arrayIntersection([1,2,2,1], [2,2]))

            