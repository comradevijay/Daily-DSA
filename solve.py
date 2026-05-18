# 1. Add two numbers
# def addTwo(a, b):
#     return a+b   
# print(addTwo(2, 5))


# 2. Even or Odd
# def evenOdd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(evenOdd(5))

# 3. Square of a number
# def sqNum(n):
#     m = n * n
#     return m 
# print(sqNum(4))

# 4. Maximum of two numbers

# def maxNum(a, b):
#     if a > b:
#         return a  
#     else:
#         return b  
# print(maxNum(28, 6))


# 5. Count elements in a list

# def findLen(arr):
#     n = len(arr)
#     return n
# print(findLen([1,2,3,4,5]))

# 6. Sum of all elements in array

# def sumArray(arr):
#     total = 0
#     for i in arr:
#         total += i
#     return total
# print(sumArray([1,2,3,4,5]))
        

# 7. Minimum element in array

# def minElement(arr):
#     minEle = float('inf')
#     for i in arr:
#         if i < minEle:
#             minEle = i    
#     return minEle
# print(minElement([3,7,3,6,2,9]))
            

# 8. Reverse a string

# def revString(s):
#     s1 = s[::-1]
#     return s1 
# print(revString("vijay"))

# 9. Count vowels in a string

# def countVowels(s):
#     vowels = 'aeiou'
#     count = 0
#     for i in s:
#         if i in vowels:
#             count += 1
#     return count  

# print(countVowels("vijay"))

# 10. Check positive, negative or zero

# def checkNum(n):
#     if n < 0:
#         return "negative"
#     elif n == 0:
#         return "zero"
#     elif n > 0:
#         return "Postive"

# print(checkNum(6))

# 11. Sum of digits of a number

# def sumDigits(n):
#     total = 0
#     for i in str(n):
#         total += int(i)
#     return total  

# print(sumDigits(121))
              

# 12. Check palindrome

# def palindrome(s):
#     if s == s[::-1]:
#         return "Yes"
#     else:
#         return "No"
# print(palindrome('madam'))

# 13. Factorial of n

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i    
#     return fact   
# print(factorial(5))

# 14. First n Fibonacci numbers

# def fibonacci(n):
#     if n == 1:
#         return [0]
    
#     fib = [0, 1]
#     while len(fib)<n:
#         fib.append(fib[-1] + fib [-2])
#     return fib  

# print(fibonacci(1)) 
    
# 15. Count even numbers in array

# def countEven(arr):
#     count = 0
#     for i in arr:
#         if i % 2 == 0:
#             count += 1
#     return count  

# print(countEven([1,2,3,4,5,6]))
    
# 16. Second largest in array

# def secLargest(arr):
#     largest = float('-inf')
#     secLargest = float('-inf')
#     for i in arr:
#         if i > largest:
#             secLargest = largest
#             largest = i   
#         elif i > secLargest and i < largest:
#             secLargest = i   
#     return secLargest

# print(secLargest([1,6,2,8,2,9,5]))

# 17. Remove duplicates from array

# def removeDuplicates(arr):
#     arr2 = []
#     for i in arr:
#         if i not in arr2:
#             arr2.append(i) 
#     return arr2

# print(removeDuplicates([1,2,3,3,4,2]))

# 18. Check if number is prime

# def primeNum(n):
#     if n <= 1:
#         return "Not prime"
#     if n == 2:
#         return "Prime"
#     if n % 2 == 0:
#         return "Not Prime"
#     for i in range(3, int(n*0.5) +1, 2):
#         if n % i == 0:
#             return "Not prime"
#     return "Prime"

# print(primeNum(4))
    

# 19. Reverse an array

# def reverseArray(arr):
#     arr2 = arr[::-1]
#     return arr2

# print(reverseArray([1,2,3,4,5]))

# 20. Most frequent element in array

# def mostFreq(arr):
#     max_count = 0
#     most_rep = arr[0]
#     for i in arr:
#         count = arr.count(i)
#         if count > max_count:
#             max_count = count
#             most_rep = i    
            
#     return most_rep

# print(mostFreq([1,2,2,3,4,2]))

# 21. Check if two strings are anagrams

# def anagrams(s1, s2):
#     if sorted(s1) == sorted(s2):
#         return "Yes"
#     else:
#         return "No"

# print(anagrams('listen', 'silent'))
    

# 22. All prime numbers from 1 to n

# def isPrime(n):
#     if n <= 1:
#         return False  
#     if n == 2:
#         return True  
#     if n % 2 == 0:
#         return False 
#     for i in range(3, int(n*0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# def allPrimes(n):
#     arr2 = []
#     for i in range(1, n+1):
#         if isPrime(i):
#             arr2.append(i)  
#     return arr2

# print(allPrimes(10))
    

# 23. Sort array ascending without sort()

# def sortArray(arr):
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr 

# print(sortArray([2,4,1,5,3,6]))
    

# 24. Find missing number in array 1 to n

# def missNum(arr):
#     actualCount = 0
#     count = 0
#     for i in range(1, len(arr)+2):
#         actualCount += i
#     for i in arr:
#         count += i
#     return abs(actualCount - count)
# 
#? -------------------------------------------
# def missNum(arr):
#     n = len(arr) + 1
#     actualSum = n * (n + 1) // 2
#     return actualSum - sum(arr)

# print(missNum([1,2,4,5]))

# 25. Count occurrences of each character

# def countOcc(s):
#     dici = {}
#     for i in s:
#         if i not in dici:
#             dici[i] = 1
#         else:
#             dici[i] += 1
#     return dici

# print(countOcc("hello"))
        
# 26. Longest word in a sentence

# def longWord(s):
#     arr2 = s.split(" ")
#     longWord = ""
#     for i in arr2:
#         if len(i) > len(longWord):
#             longWord = i   
#     return longWord 

# print(longWord("i love programing"))

# 27. Check if array is sorted

# def checkSorted(arr):
#     if arr == sorted(arr):
#         return "Yes"
#     else:
#         return "No"

# print(checkSorted([3,1,2,3,4,5]))
#? -------------------------------------------- 
# def checkSorted(arr):
#     for i in range(len(arr) -1):
#         if arr[i] > arr[i+1]:
#             return "No"
#     return "Yes"
    
# print(checkSorted([3,1,2,3,4,5]))

# 28. Common elements in two arrays

# def findCommon(arr1, arr2):
#     arr3 = []
#     for i in arr1:
#         if i in arr2 and i not in arr3 :
#             arr3.append(i)  
#     return arr3

# print(findCommon([1,2,3,5], [2,3,4]))
        

# 29. Flatten a nested list

# def flattenList(arr):
#     arr2 = []
#     for i in arr:
#         arr2 += i   
#     return arr2  

# print(flattenList([[1,2,3],[2,3],[8,2,1]]))

# 30. Find pair of numbers that add up to target

# def twoSum(arr, target):
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 return [arr[i], arr[j]]
#     return []

# print(twoSum([1,2,3,4,5], 5))
#? ---------------------------------------------------
# def twoSum(arr, target):
#     seen = set()  
#     for num in arr:
#         temp =  target - num 
#         if temp in seen:
#             return temp, num 
#         seen.add(num)
#     return []

# print(twoSum([1,2,3,4,5], 5))


# 31. Longest substring without repeating characters

# def subString(s): 
#     seen = set() 
#     l = 0
#     ans = 0
#     for r in range(len(s)):
#         while s[r] in seen:
#             seen.remove(s[l])
#             l += 1
#         seen.add(s[r])
#         ans = max(ans, r-l+1)
#     return ans  

# print(subString('abcabcbb'))
    
    

# 32. Count pairs with given sum

# def countPairs(arr, total):
#     count = 0
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == total:
#                 count += 1
#     return count  

# print(countPairs([1,2,3,4,5], 5))
            
        

# 33. Rotate array by k positions

# def rotateArray(arr, k):
#     k = k % len(arr)
#     arr[:] = arr[-k:] + arr[:-k]
#     return arr

# print(rotateArray([1,2,3,4,5], 2))

# 34. Check if brackets are balanced

# def isValid(s):
#     seen = []
#     for i in s:
#         if i == '(':
#             seen.append(')')
#         elif i == '{':
#             seen.append('}')
#         elif i == '[':
#             seen.append(']')
#         elif not seen or seen.pop() != i:
#             return "No"
#     if len(seen) == 0:
#         return "Yes"
#     else:
#         return "No"
    
# print(isValid('{[]()}'))
    

# 35. Find all duplicates in array

# def allDuplicates(arr):
#     dup = []
#     seen = set() 
#     for i in arr:
#         if i in seen:
#             dup.append(i)  
#         else:
#             seen.add(i)
#     return dup   

# print(allDuplicates([1,5,1,2,5,2,8,9,4]))