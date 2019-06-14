def fibo(num):
    if num==1:
        return 0
    elif num==2:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)
        
def fiboseries(n):
    for i in range(1,n+1):
        print(fibo(i))
fiboseries(5)
