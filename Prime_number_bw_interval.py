def isprime(num):
    if num==1:
        return False
    else:
        for i in range(2,num//2):
            if num%i==0:
                return False
    return True
(start,end)=(1,100)
for i in range(start,end+1):
    if isprime(i):
        print(i)
