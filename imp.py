# 14. First n Fibonacci numbers

# def fibonacci(n):
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     fib = [0, 1]
#     while len(fib) < n:
#         fib.append(fib[-1] + fib[-2])
#     return fib  

# print(fibonacci(5))

# 20. Most frequent element in array

# def mostFreq(arr):
#     maxCount = 0
#     mostFreq = arr[0]
#     for i in arr:
#         count = arr.count(i)
#         if count > maxCount:
#             maxCount = count
#             mostFreq = i
#     return mostFreq 

# print(mostFreq([1,2,3,4,3]))

# 22. All prime numbers from 1 to n

# def isPrime(n):
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
    
# def allPrimes(n):
#     arr = []
#     for i in range(n+1):
#         if isPrime(i):
#             arr.append(i)
#     return arr 

# print(allPrimes(10))


# 25. Count occurrences of each character

# def countOcc(s):
#     dici = {}
#     for i in s:
#         if i not in dici:
#             dici[i] = 1
#         else:
#             dici[i] += 1
#     return dici   

# print(countOcc('hello'))

# 29. Flatten a nested list

# def flattenList(arr):
#     arr2 = []
#     for i in range(len(arr)):
#         arr2 += arr[i] 
#     return arr2

# print(flattenList([[1,2,3],[4,5],[6]]))  
            
        

# 31. Longest substring without repeating characters

# def subString(s):
#     l = 0
#     seen = set() 
#     ans = 0
#     for r in range(len(s)):
#         while s[r] in seen:
#             seen.remove(s[l])
#             l += 1
#         seen.add(s[r])
#         ans = max(ans, r-l+1)
#     return ans  

# print(subString('abcabcbb'))
    



#todo New
# IBM Coding Practice Questions

#! Arrays

#? 1. Find the largest element in an array.
#    Input: [4, 7, 1, 9, 2]
#    Output: 9

# def largest(arr):
#     largest = float('-inf')
#     for i in arr:
#         if i > largest:
#             largest = i  
#     return largest

# print(largest([4, 7, 1, 9, 2]))

#? 2. Find the second largest element in an array.
#    Input: [4, 7, 1, 9, 2]
#    Output: 7

# def secLargest(arr):
#     largest, secLargest = float('-inf'), float('-inf')
#     for i in arr:
#         if i > largest:
#             secLargest = largest
#             largest = i   
#         elif i > secLargest and i < largest:
#             secLargest = i   
#     return secLargest 

# print(secLargest([4, 7, 1, 9, 2]))

#? 3. Reverse an array.
#    Input: [1, 2, 3, 4]
#    Output: [4, 3, 2, 1]

# def revArray(arr):
#     arr2 = arr[::-1]
#     return arr2  

# print(revArray([1, 2, 3, 4]))

#? 4. Remove duplicates from an array.
#    Input: [1, 2, 2, 3, 4, 4]
#    Output: [1, 2, 3, 4]

# def removeDup(arr):
#     arr2 = []
#     for i in arr:
#         if i not in arr2:
#             arr2.append(i)   
#     return arr2

# print(removeDup([1,1,2,3,2,4,5]))
        

#? 5. Find the most repeating element in an array.
#    Input: [1, 1, 2, 3, 3, 3]
#    Output: 3

# def mostRep(arr):
#     maxCount = 0 
#     mostRep = arr[0]
#     for i in arr:
#         count = arr.count(i)  
#         if count > maxCount:
#             maxCount = count
#             mostRep = i   
#     return mostRep 

# print(mostRep([1, 1, 2, 3, 3, 3]))

#? 6. Find the sum of all elements in an array.
#    Input: [1, 2, 3, 4]
#    Output: 10

# def sumArray(arr):
#     total = 0
#     for i in arr:
#         total += i
#     return total 

# print(sumArray([1, 2, 3, 4]))

#? 7. Find the minimum element in an array.
#    Input: [8, 3, 5, 1, 9]
#    Output: 1

# def minElement(arr):
#     minEle = float('inf')
#     for i in arr:
#         if i < minEle:
#             minEle = i    
#     return minEle

# print(minElement([8, 3, 5, 1, 9]))

#? 8. Check if an array is sorted.
#    Input: [1, 2, 3, 4, 5]
#    Output: Sorted

# def checkSorted(arr):
#     for i in range(len(arr)):
#         if arr[i] > arr[i+1]:
#             return "Unsorted"
#         else:
#             return 'sorted'
# print(checkSorted([1, 2, 3, 4, 5]))

#? 9. Merge two arrays.
#    Input: [1, 2, 3] [4, 5, 6]
#    Output: [1, 2, 3, 4, 5, 6]

# def mergeArrays(arr1, arr2):
#     arr3 = arr1 + arr2
#     return arr3

# print(mergeArrays([1,2,3],[4,5,6]))

#? 10. Find duplicates in an array.
#     Input: [1, 2, 3, 2, 4, 1]
#     Output: [1, 2]

# def findDup(arr):
#     arr2 = []
#     for i in arr:
#         if arr.count(i) > 1 and i not in arr2:
#             arr2.append(i)
#     return arr2

# print(findDup([1, 2, 3, 2, 4, 1]))

#! Strings
#? 11. Reverse a string.
#     Input: hello
#     Output: olleh

# def revString(s):
#     s2 = s[::-1]
#     return s2  

# print(revString('vijay'))

#? 12. Check if a string is palindrome.
#     Input: madam
#     Output: Palindrome

# def palindrome(s):
#     if s == s[::-1]:
#         return "Palindrome"
#     else:
#         return "Not palindrome"
# print(palindrome('madam'))

#? 13. Count vowels in a string.
#     Input: education
#     Output: 5

# def countVowels(s):
#     count = 0
#     for i in s:
#         if i in 'aeiou':
#             count += 1
#     return count  

# print(countVowels('education'))

#? 14. Check whether two strings are anagrams.
#     Input: listen silent
#     Output: Anagram

# def  anagram(s1,s2):
#     if sorted(s1) == sorted(s2):
#         return 'Anagram'
#     else:
#         return 'Not Anagram'
# print(anagram('listen', 'silent'))

#? 15. Find duplicate characters in a string.
#     Input: programming
#     Output: r g m

# def dupChar(s):
#     s2 = ''
#     for i in s:
#         if s.count(i) > 1 and i not in s2:
#             s2 += i + " " 
#     return s2  

# print(dupChar('programming'))

#? 16. Count words in a sentence.
#     Input: I love python programming
#     Output: 4

# def countWords(s):
#     arr = s.split(" ")
#     return len(arr)
# print(countWords('I love python programming'))

#? 17. Convert lowercase string to uppercase.
#     Input: python
#     Output: PYTHON

# def convertUpper(s):
#     s2 = s.upper()
#     return s2  
# print(convertUpper('python'))

#? 18. Remove spaces from a string.
#     Input: hello world
#     Output: helloworld

# def removeSpace(s):
#     arr = s.strip().split()
#     s2 = ''
#     for i in arr:
#         s2 += i   
#     return s2  

# print(removeSpace('hello world'))

#? 19. Find the length of a string without using len().
#     Input: hello
#     Output: 5

# def strLen(s):
#     count = 0
#     for i in s:
#         count += 1
#     return count   

# print(strLen('hello'))
        
        

#? 20. Find the first non-repeating character in a string.
#     Input: swiss
#     Output: w

# def firstNonrep(s):
#     for i in s:
#         if s.count(i) == 1:
#             return  i   

# print(firstNonrep('swiss'))

# HashMap / Dictionary

#? 21. Count frequency of elements in an array.
#     Input: [1, 2, 2, 3, 1, 1]
#     Output: {1:3, 2:2, 3:1}

# def countFreq(arr):
#     dici = {}
#     for i in arr:
#         if i in dici:
#             dici[i] += 1
#         else:
#             dici[i] = 1
#     return dici   

# print(countFreq([1, 2, 2, 3, 1, 1]))

#? 22. Find the first non-repeating element in an array.
#     Input: [1, 2, 2, 3, 1, 4]
#     Output: 3

# def nonRep(arr):
#     for i in arr:
#         if arr.count(i) == 1:
#             return i

# print(nonRep([1, 2, 2, 3, 1, 4]))

#? 23. Find the element with maximum frequency.
#     Input: [4, 4, 2, 1, 4, 2]
#     Output: 4

# def maxFreq(arr):
#     maxCount = 0
#     maxFreq = arr[0]
#     for i in arr:
#         count = arr.count(i)  
#         if count > maxCount:
#             maxCount = count  
#             maxFreq = i   
#     return maxFreq

# print(maxFreq([4, 4, 2, 1, 4, 2]))

#? 24. Count frequency of characters in a string.
#     Input: apple
#     Output: {a:1, p:2, l:1, e:1}

# def countFreq(s):
#     dici = {}
#     for i in s:
#         if i in dici:
#             dici[i] += 1
#         else:
#             dici[i] = 1
#     return dici   

# print(countFreq('apple'))
            
            

#? 25. Check if two arrays contain same elements.
#     Input: [1,2,3] [3,2,1]
#     Output: Yes

# def chekArray(arr1, arr2):
#     if sorted(arr1) == sorted(arr2):
#         return "Yes"
#     else:
#         return "No"
    
# print(chekArray([1,2,3], [3,2,1]))
    

#! Sorting

#? 26. Sort an array using bubble sort.
#     Input: [5, 2, 8, 1]
#     Output: [1, 2, 5, 8]

# def bubbleSort(arr):
#     for i in range(len(arr)):
#         for j in range(0, len(arr)-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# print(bubbleSort([5, 2, 8, 1]))
             

#? 27. Sort an array in descending order.
#     Input: [4, 1, 7, 3]
#     Output: [7, 4, 3, 1]

# def sortDesc(arr):
#     for i in range(len(arr)):
#         for j in range(0, len(arr)-1-i):
#             if arr[j] < arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# print(sortDesc([4, 1, 7, 3]))

#? 28. Sort a string alphabetically.
#     Input: python
#     Output: hnopty

# def sortString(s):
#     arr =  sorted(s)
#     sortedString = ''
#     for i in arr:
#         sortedString += i   
#     return sortedString

# print(sortString('python'))

#? 29. Sort only even numbers in an array.
#     Input: [5, 2, 8, 1, 4]
#     Output: [5, 2, 4, 1, 8]

# def sortEven(arr):
#     for i in range(len(arr)-1):
#         if arr[i] % 2==0:
#             for  j in range(i+1, len(arr)):
#                 if arr[j] % 2 == 0 and arr[i] > arr[j]:
#                     arr[i], arr[j] = arr[j], arr[i]
#     return arr  

# print(sortEven([5, 2, 8, 1, 4]))

#? 30. Find kth largest element in an array.
#     Input: [3, 1, 5, 2, 4], k = 2
#     Output: 4

# def kthLargest(arr, k):
#     arr2 = sorted(arr)
#     arr2 = arr2[::-1]
#     return arr2[k-1]
# print(kthLargest([3, 1, 5, 2, 4], k = 2))



#! Find GCD of two numbers.
#   Input: 12 18
#   Output

# def findGcd(a,b):
#     while b !=0:
#         a,b = b,a%b   
#     return a

# print(findGcd(48, 18))


#! Check whether a number is Armstrong.
#   Input: 153
#   Output: Armstrong

# def amstrong(num):
#     numStr = str(num)
#     n = len(numStr)
#     totalSum = sum(int(digit) ** n for digit in numStr)
#     if totalSum == num:
#         return 'Amstrong'
#     else:
#         return 'Not amstrong'

# print(amstrong(153))

def minWords(arr, potion):
    needed = set(potion)
    result = []
    
    while needed:
        bestWord = ""
        covered = set()   
        for word in arr:
            common = needed & set(word)
            if len(common) > len(covered):
                bestWord = word   
                covered = common
        result.append(bestWord)
        needed -= covered
    
    return result

print(minWords(['ram', 'vijay', 'krish'], 'isha'))