
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

#! 121. Best Time to Buy and Sell Stock
#? Input: prices = [7,1,5,3,6,4]
#? Output: 5

def maxProfit(prices):
    
    # minVal = prices[0]
    # ans = 0
    # for i in range(1,len(prices)):
    #     ans = max(ans, prices[i] - minVal)
    #     minVal = min(minVal, prices[i])
    # return ans 

    min_price = prices[0]
    max_profit = 0 
    for price in prices:
        profit  = price - min_price
        if price < min_price:
            min_price = price
        if profit > max_profit:
            max_profit = profit 
    return max_profit

# print(maxProfit([7,1,5,3,6,4]))


#! 3783. Mirror Distance of an Integer
#? Input: n = 25
#? Output: 27

def mirrorDistance(n):
    return abs(n - int(str(n)[::-1]))

# print(mirrorDistance(25))

#! 2894. Divisible and Non-divisible Sums Difference
#? Input: n = 10, m = 3
#? Output: 19

def differenceOfSums(n, m):
    num1 = 0
    num2 = 0
    for i in range(1,n+1):
        if i%m!=0:
            num1+=i
        else:
            num2+=i
    return num1 - num2 

# print(differenceOfSums(10, 3))

#! 3190. Find Minimum Operations to Make All Elements Divisible by Three
#? Input: nums = [1,2,3,4]
#? Output: 3

def minimumOperations(nums):
    count = 0
    for i in nums:
        if i%3 != 0:
            count+=1 
    return count

# print(minimumOperations([1,2,3,4]))

#! 3701. Compute Alternating Sum
#? Input: nums = [1,3,5,7]
#? Output: -4

def alternatingSum(nums):
    
    total = 0
    for i in range(len(nums)):
        if i%2 == 0:
            total +=  nums[i]
        else:
            total -= nums[i]
    return total
    
    # if len(nums) == 1:
    #     return nums[0]
    # for i in range(len(nums)):
    #     if i%2 != 0:
    #         nums[i] = nums[i]*-1
    # return sum(nums)

# print(alternatingSum([1,3,5,7]))

#! 2535. Difference Between Element Sum and Digit Sum of an Array
#? Input: nums = [1,15,6,3]
#? Output: 

def differenceOfSum(nums):
    elementSum = 0
    for i in nums:
        elementSum+=i   
    str1 = ''
    for i in nums:
        str1 += str(i)   
    digitSum = 0
    for i in range(len(str1)):
        digitSum += int(str1[i])
    
    return elementSum - digitSum

# print(differenceOfSum([1,15,6,3]))

#! 3895. Count Digit Appearances
#? Input: nums = [12,54,32,22], digit = 2
#? Output: 4

def countDigitOccurrences(nums, digit):
    str1 = ''
    count = 0
    for i in nums:
        str1 += str(i)   
    for i in str1:
        if i == str(digit):
            count+=1 
    return count  

# print(countDigitOccurrences([12,54,32,22], 2))

#! 1688. Count of Matches in Tournament
#? Input: n = 7
#? Output: 6

def numberOfMatches(n):
    
    # return n-1  

    res = 0
    while n > 1:
        res += n // 2
        n = (n // 2) + (n % 2)
    return res

# print(numberOfMatches(7))

#! 1662. Check If Two String Arrays are Equivalent
#? Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
#? Output: true

def arrayStringsAreEqual(word1, word2):
    str1 = ''
    str2 = ''
    for i in word1:
        str1 += i   
    for i in word2:
        str2 += i   
    
    if str1 == str2:
        return True
    else:
        return False  
    
# print(arrayStringsAreEqual(["ab", "c"], ["a", "bc"])) 

#! 2652. Sum Multiples
#? Input: n = 7
#? Output: 21

def sumOfMultiples(n):
    total = 0
    for i in range(1,n+1):
        if i%3 == 0 or i%5 == 0 or i%6 == 0 or i%7 == 0:
            total += i  
    return total 

# print(sumOfMultiples(7))

#! 2553. Separate the Digits in an Array
#? Input: nums = [13,25,83,77]
#? Output: [1,3,2,5,8,3,7,7]

def separateDigits(nums):
    str1 = ''
    arr = []
    for i in nums:
        str1 += str(i) 
    for j in str1:
        arr.append(int(j))
    return arr

# print(separateDigits([13,25,83,77]))

#! 709. To Lower Case
#? Input: s = "Hello"
#? Output: "hello"

def toLowerCase(s):
    str1 = ''
    arr = []
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            arr.append(ord(i) + 32) 
        else:
            arr.append(ord(i))
    for i in arr:
        str1 += chr(i)
    return str1 
# print(toLowerCase("Hello"))


#! 344. Reverse String
#? Input: s = ["h","e","l","l","o"]
#? Output: ["o","l","l","e","h"]

def reverseString(s):
    l = 0
    r = len(s) -1 
    while l < r:
        temp = s[l]
        s[l] = s[r]
        s[r] = temp 
        
        l += 1
        r -= 1
    return s    

# print(reverseString(['H', 'e', 'l', 'l', 'o']))
