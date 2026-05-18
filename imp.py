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

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n*0.5)+1, 2):
        if n % i == 0:
            return False
    return True
    
def allPrimes(n):
    arr = []
    for i in range(n+1):
        if isPrime(i):
            arr.append(i)
    return arr 

print(allPrimes(10))


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
    