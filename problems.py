
#! 1. Add two numbers given as parameters
#?    Input: a=3, b=5 → Output: 8

# def addTwo(a,b):
#     return a+b 

# ans = addTwo(2,5)
# print(ans) 
    
#! 2. Find if a number is even or odd
#?    Input: n=7 → Output: "Odd"

# def evenOdd(n):
#     if n % 2 == 0:
#         return "Yes"
#     else: 
#         return "No"
    
# ans = evenOdd(6)
# print(ans)

#! 3. Return the square of a number
#?    Input: n=4 → Output: 16

# def sqNum(n):
#     n = n*n 
#     return n   
# ans = sqNum(2)

# print(ans)

#! 4. Find maximum of two numbers
#?    Input: a=10, b=20 → Output: 20

# def maxNum(n, m):
#     if n > m:
#         return n 
#     else:
#         return m 
    
# ans = maxNum(9, 8)
# print(ans)

#! 5. Count how many elements in a list
#?    Input: arr=[1,2,3,4] → Output: 4

# def findLen(arr):
#     length = len(arr)
#     return length  

# ans = findLen([1,2,3,4,5])
# print(ans)

#! 6. Find sum of all elements in array
#?    Input: arr=[1,2,3,4,5] → Output: 15

# def sumArray(arr):
#     result = 0
#     for i in arr:
#         result += i   
#     return result  

# ans = sumArray([1,2,3,4,5])
# print(ans)
    
#! 7. Find minimum element in array
#?    Input: arr=[3,1,4,1,5] → Output: 1

# def minElement(arr):
#     minEle = float('inf')
#     for i in arr:
#         if i < minEle:
#             minEle = i   
#     return minEle

# ans = minElement([5,2,3,6,4])
# print(ans)

#! 8. Reverse a string
#?    Input: s="hello" → Output: "olleh"

# def revString(s):
#     ans = s[::-1]
#     return ans

# ans = revString("hello")
# print(ans)

#! 9. Count vowels in a string
#?    Input: s="hello" → Output: 2

# def countVowels(s):
#     count = 0
#     for ch in s:
#         if ch in 'aeiou':
#             count +=1
#     return count  

# ans = countVowels("vijay")
# print(ans)

#! 10. Check if number is positive, negative or zero
#?   Input: n=-5 → Output: "Negative"

# def checkNum(n):
#     if n > 0 :
#         return "Positive"
#     elif n == 0:
#         return "zero"
#     else: 
#         return "negative"

# ans = checkNum(-7)
# print(ans)

#! 11. Return sum of digits of a number
#?     Input: n=123 → Output: 6


# def sumDigits(s):
#     sumDig = 0
#     for i in str(s):
#         sumDig += int(i) 
#     return sumDig

# ans = sumDigits(121)
# print(ans)

#! 12. Check if a string is palindrome
#?     Input: s="madam" → Output: "Yes"

# def palindrome(s):
#     if s == s[::-1]:
#         return "YES"
#     else:
#         return "NO"

# ans = palindrome("madm")
# print(ans) 


#! 13. Find factorial of n
#?    Input: n=5 → Output: 120


# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i   
#     return fact   

# ans = factorial(5)
# print(ans)

#! 14. Print first n Fibonacci numbers
#?    Input: n=5 → Output: [0,1,1,2,3]

# def fibonacci(n):
#     if n <= 0 :
#         return []
#     if n == 1:
#         return [0]
    
#     fib = [0, 1]
#     while len(fib) < n:
#         fib.append(fib[-1] + fib[-2])
#     return fib   

# ans = fibonacci(5)
# print(ans)

#! 15. Count how many even numbers in array
#?    Input: arr=[1,2,3,4,6] → Output: 3

# def countEven(arr):
#     count = 0
#     for i in arr:
#         if i % 2 == 0:
#             count +=1
#     return count  

# ans = countEven([1,2,3,2,4,5,8])
# print(ans)


#! 16. Find second largest in array
#?    Input: arr=[3,1,4,1,5,9] → Output: 5

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

# ans = secLargest([2,4,2,5,8,7])
# print(ans)

#! 17. Remove duplicates from array
#?    Input: arr=[1,2,2,3,3,4] → Output: [1,2,3,4]

# def removeDuplicates(arr):
#     arr2 = []
#     for i in arr:
#         if i not in arr2:
#             arr2.append(i)
        
#     return arr2 

# ans = removeDuplicates([2,4,2,5,1,6])
# print(ans)


#! 18. Check if number is prime
#?    Input: n=7 → Output: "Prime"

# def primeNum(n):
#     if n <= 1:
#         return False  
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n*0.5)+1, 2):
#         if n % i == 0:
#             return False
#     return True

# ans = primeNum(5)
# print(ans)

#! 19. Reverse an array
#?    Input: arr=[1,2,3,4,5] → Output: [5,4,3,2,1]

# def reverseArray(arr):
#     arr2 = arr[::-1]
        
#     return arr2  

# ans = reverseArray([1,2,3,4,5])
# print(ans)

#! 20. Find most frequent element in array
#?    Input: arr=[1,2,2,3,2] → Output: 2

# def mostFreq(arr):
    
#     max_count = 0
#     most_rep = arr[0]
    
#     for i in arr:
#         count = arr.count(i)   
#         if count > max_count:
#             max_count = count
#             most_rep = i
#     return most_rep

#  ------------------------------
    # arr.sort()
    # temp = len(arr)//2
    # print(arr)
    # return arr[temp]

# ans = mostFreq([1,1,2,4,2,4,5,4,3])
# print(ans)

#! 21. Check if two strings are anagrams
#?   Input: s1="listen", s2="silent" → Output: "Yes"

# def anagrams(s1, s2):
#     if len(s1) != len(s2):
#         return "No"
#     if(sorted(s1) == sorted(s2)):
#         return "Yes"
#     else:
#         return "No"

# ans = anagrams("silent", "listen")
# print(ans)


#! 22. Find all prime numbers from 1 to n
#?    Input: n=10 → Output: [2,3,5,7]

# def isPrime(n):
#     if n <= 1:
#         return False  
#     if n == 2:
#         return True 
#     if n % 2 == 0:
#         return False
#     for i in range(2, int(n*0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# def primeNum(n):
#     arr = []
#     for i in range(1,n+1):
#         if isPrime(i):
#             arr.append(i)
#     return arr
    
    
# ans = primeNum(10)
# print(ans)


#! 23. Sort array in ascending order (without sort())
#?    Input: arr=[3,1,4,1,5] → Output: [1,1,3,4,5]

# def sortArray(arr):
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
                
#     return arr

# ans = sortArray([3,1,4,1,5])
# print(ans)


#! 24. Find missing number in array 1 to n
#?    Input: arr=[1,2,4,5], n=5 → Output: 3

# def missNum(arr):
#     n = len(arr) +1
#     actualSum = n * (n + 1) // 2
#     return actualSum - sum(arr)

# ans = missNum([1,2,4,5])
# print(ans)


#! 25. Count occurrences of each character in string
#?    Input: s="hello" → Output: h=1,e=1,l=2,o=1

# def countOcc(s):
#     dici = {}
#     for i in s:
#         if i not in dici:
#             dici[i] = 1
#         else:
#             dici[i]+=1
#     return dici   

# ans = countOcc("hello")
# print(ans)

#! 26. Find longest word in a sentence
#?    Input: "I love programming" → Output: "programming"

# def longWord(s):
#     wordArray = s.split()
#     longWord = ""
#     for i in wordArray:
#         if len(i) > len(longWord):
#             longWord = i
#     return longWord

# ans = longWord("I love programming")
# print(ans)


#! 27. Check if array is sorted
#?    Input: arr=[1,2,3,4,5] → Output: "Yes"


# def checkSorted(arr):
#     for i in range(len(arr) -1):
#         if arr[i] > arr[i+1]:
#             return "No"
#     return "Yes"

# ans = checkSorted([1,2,3,4,5,6])
# print(ans)


#! 28. Find common elements in two arrays
#?    Input: [1,2,3], [2,3,4] → Output: [2,3]

# def findCommon(arr1, arr2):
#     arr3 = []
#     for i in arr1:
#         if i in arr2 and i not in arr3:
#             arr3.append(i)   
#     return arr3

# ans = findCommon([1,2,3], [2,3,4])
# print(ans)

#! 29. Flatten a nested list
#?    Input: [[1,2],[3,4],[5]] → Output: [1,2,3,4,5]

# def flattenList(arr):
#     arr2 = []
#     for i in arr:
#         arr2 += i   
#     return arr2  

# ans = flattenList([[1,2],[3,4],[5]] )
# print(ans)
#? ---------------------------------------------------- 
# def flattenList(arr):
#     arr2 = []
#     for i in arr:
#         if isinstance(i, list):
#             arr2.extend(flattenList(i))
#         else:
#             arr2.append(i)
#     return arr2

# ans = flattenList([[1,2],[3,4],[5]] )
# print(ans)

#! 30. Find pair of numbers that add up to target
#?    Input: arr=[1,2,3,4], target=5 → Output: (1,4) or (2,3)

# def twoSum(arr, target):
#     for i in range(len(arr)-1):
#         for j in range(i+1,len(arr)):
#             if arr[i] + arr[j] == target:
#                 return arr[i], arr[j]
#     return []

# ans = twoSum([1,2,3,4], 5)
# print(ans)
#? -------------------------------------------------
# def twoSum(arr, target):
#     seen = set() 
#     for num in arr:
#         temp = target - num
#         if temp in seen:
#             return temp, num 
#         seen.add(num)
#     return []

# ans = twoSum([1,2,3,4], 5)
# print(ans)

#! 31. Find longest substring without repeating characters
#?    Input: s="abcabcbb" → Output: 3 ("abc")

# def subString(s):
#     n = len(s)
#     seen = set()
#     l = 0
#     ans = 0
#     for r in range(n):
#         while s[r] in seen:
#             seen.remove(s[l])
#             l += 1
#         seen.add(s[r])
#         ans = max(ans, abs(r-l)+1)
#     return ans

# result = subString("pwwkew")
# print(result)

#! 32. Count pairs with given sum
#? Input: arr=[1,2,3,4,5], sum=5 → Output: 2 (pairs: 1+4, 2+3)

# def countPairs(arr, sum):
#     count = 0
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == sum:
#                 count += 1
#     return count   

# ans = countPairs([1,2,3,4,5], 5)
# print(ans)
#?--------------------------------------------------- 
# def countPairs(arr, sum):
#     count = 0
#     seen = set() 
#     for num in arr:
#         temp = sum - num
#         if num in seen:
#             count += 1 
#         seen.add(temp)
#     return count

# result = countPairs([1,2,3,4,5], 5)
# print(result)
    
#! 33. Rotate array by k positions
#?    Input: arr=[1,2,3,4,5], k=2 → Output: [4,5,1,2,3]

# def rotateArray(arr, k):
#     n = len(arr)
#     rotations = k % n
#     for i in range(rotations):
#         last_ele = arr.pop()
#         arr.insert(0, last_ele)
#     return arr

# result = rotateArray([1,2,3,4,5], 3)
# print(result)
#? -------------------------------------------------------
# def rotateArray(arr, k):
#     k = k % len(arr) 
    
#     return arr[-k:] + arr[:-k]
    
    
# result = rotateArray([1,2,3,4,5], 3)
# print(result)


#! 34. Check if brackets are balanced
#?    Input: s="(()())" → Output: "Yes"
#?    Input: s="(()" → Output: "No"

# def isValid(s):
#     stack = []
#     for c in s:
#         if c == '(':
#             stack.append(')')
#         elif c == '{':
#             stack.append('}')
#         elif c == '[':
#             stack.append(']')
#         elif not stack or stack.pop() != c :
#             return "No"
#     if len(stack) == 0:
#         return "Yes"
#     else:
#         return "No"
# ans = isValid("}")
# print(ans)
            


#! 35. Find all duplicates in array
#?     Input: arr=[1,2,3,2,4,3] → Output: [2,3]

# def allDuplicates(arr):
#     seen = set() 
#     dup = []
#     for  i in arr:
#         if i in seen:
#             dup.append(i)  
#         seen.add(i)
#     return dup  

# ans = allDuplicates([1,2,3,4,2,3])
# print(ans)



#todo Additional Problems


#! largest in an array 

# def largest(arr):
#     max_val = arr[0]
#     for i in arr:
#         if i > max_val:
#             max_val = i   
#     return max_val

# ans = largest([1,2,7,4,3])

# print(ans)

#! thrid largest in array

# def thridLargest(arr):
#     largest = float('-inf')
#     secLargest = float('-inf')
#     thridLargest = float('-inf')
    
#     for i in arr:
#         if i > largest:
#             thridLargest = secLargest
#             secLargest = largest
#             largest = i 
#         elif i > secLargest and i < largest:
#             thridLargest = secLargest 
#             secLargest = i   
#         elif i > thridLargest and i < secLargest:
#             thridLargest = i   
#     return thridLargest

# ans = thridLargest([2,4,6,2,7,2,9,3]) 
# print(ans)


#! Substrings of Size Three

# def subString(s):
#     n = len(s)
#     l = 0
#     ans = 0
#     dici = {}
#     k = 3
#     for r in range(n):
#         if s[r] in dici:
#             dici[s[r]] += 1
#         else:
#             dici[s[r]] = 1
        
#         if r-l ==k:
#             dici[s[l]] -= 1
#             if dici[s[l]] == 0:
#                 dici.pop(s[l])
#             l+=1
            
#         if len(dici) == k:
#             ans += 1
#     return ans

# result = subString("xyzzaz")
# print(result)

