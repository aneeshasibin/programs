str=input("Enter the string:")
s=[]
vowels=['a','e','i','o','u']
for i in str:
    if i in vowels:
        s.append(i)
print("Number of vowels in string is",len(s))