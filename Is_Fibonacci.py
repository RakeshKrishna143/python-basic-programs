import math
def isPerfectSquare(n):
    s=int(math.sqrt(n))
    if pow(s,2)==n:
        return True
    return False
def isFibonacci(n):
    return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)
print(isFibonacci(9))
    
