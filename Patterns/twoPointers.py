
#! Two Pointers Pattern

#! opposite directions
#? one pointer from the start and one pointer from the end of the array. 
#? Move the pointers towards each other until they meet. 
#? This pattern is often used to solve problems that involve searching for pairs or triplets in a sorted array.

#! example problem: 167. Two Sum II - Input Array Is Sorted
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

def twoSum(numbers, target):
    l = 0
    r = len(numbers) -1
    while l < r:
        currSum = numbers[l] + numbers[r]
        if currSum == target:
            return [l+1, r+1]
        elif currSum < target:
            l += 1
        else:
            r -= 1
    return []

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))



#! fast & slow pointers
#? one pointer moves faster than the other.
#? The fast pointer moves two steps at a time, while the slow pointer moves one step at a time.
#? This pattern is often used to solve problems that involve finding the middle of a linked list, 
#? detecting cycles in a linked list, or finding the nth node from the end of a linked list.

#! Partition & Merge Patterns
#? Partitioning an array involves dividing it into two or more subarrays based on a certain condition.
#? Merging involves combining two or more sorted arrays into a single sorted array. 



