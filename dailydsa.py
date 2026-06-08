
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

#! 88. Merge Sorted Array
#? Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#? Output: [1,2,2,3,5,6]

def mergeSortedArray(nums1, m, nums2, n):
    nums1[m:] = nums2[:n]
    nums1.sort()
    
    print(nums1) 

    i = len(nums1)-m   
    j = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == 0:
                nums1[i], nums2[j] = nums2[j], nums1[i]
    nums1.sort()
    return nums1 

# print(mergeSortedArray([1,2,3,0,0,0], 3, [2,5,6], 3))

#! 977. Squares of a Sorted Array
#? Input: nums = [-4,-1,0,3,10]
#? Output: [0,1,9,16,100]

def sortedSquares(nums):
    for i in range(len(nums)):
        nums[i] = abs(nums[i])*abs(nums[i])
        print(nums[i])
    nums.sort()
    return nums


# print(sortedSquares([-4,-1,0,3,10]))

#! 136. Single Number
#? Input: nums = [4,1,2,1,2]
#? Output: 4

def singleNumber(nums):
    for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
            return nums[i]
    
    # -----------------------------------
    
    m = 0
    for i in nums:
        m = m^i    
    return m

# print(singleNumber([2,2,1]))

#! 3512. Minimum Operations to Make Array Sum Divisible by K
#? Input: nums = [3,9,7], k = 5
#? Output: 4

def minOperations(nums, k):
    total = 0
    for i in nums:
        total += i   
    return total % k   

    # return sum(nums) % k

# print(minOperations([3,9,7], 5))