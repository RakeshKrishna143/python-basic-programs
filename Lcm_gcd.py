def divisibility(a,n):
    return all(i%n==0 for i in a)
a=[24,54]
c=[i for i in range(1,min(a)+1) if divisibility(a,i)]
p=1
for i in a:
    p=p*i
print(p//max(c))
