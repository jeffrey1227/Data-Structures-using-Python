# Recursion

# def recursiveFactorial(num):
#     if num == 1:
#         return 1

#     return num * recursiveFactorial(num-1)

# print(recursiveFactorial(6))

import time

def loopFibonacci(n):
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-2] + arr[i-1])
    return arr[n]


def recursiveFibonacci(num):
    if num < 2:
        return num

    return recursiveFibonacci(num-1) + recursiveFibonacci(num-2)

start = time.time()
print(recursiveFibonacci(25))
end = time.time()
print(end - start)

start = time.time()
print(loopFibonacci(25))
end = time.time()
print(end - start)



# Implement a function that reverses a string using iteration...and then recursion!
def loopReverseString(str):
    revStr = ''
    for i in range(len(str)):
        revStr += str[len(str)-1-i]

    return revStr


def recursiveReverseString(str):
    if str == "":
        return ""
    return str[-1] + recursiveReverseString(str[:-1])



print(loopReverseString('yoyo mastery'))
print(recursiveReverseString('yoyo mastery'))
# should return: 'yretsam oyoy'