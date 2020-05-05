'''

Engineer's Revolution
Program to count number of vowels in a string 

'''

s = input()
vowel = 'aeiouAEIOU'
count = 0
for i in s:
    if i in vowel:
        count += 1
        
print(count)
