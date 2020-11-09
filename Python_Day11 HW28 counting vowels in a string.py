s=input("Enter a string : ")
v=['a','e','i','o','u','A','E','I','O','U']
cnt=0
for ch in s :
    if ch in v :
        cnt = cnt+1
        
print("Number of vowels = ",cnt)
print("Number of consonents = ",len(s)-cnt)

input()
