str=input("Enter the string:")
vowels=['a','e','i','o','u']
s=[]
for i in str:
    if i in vowels:
        s.append(i)
if len(s)==len(vowels):
    print("Accepted")
else:
    print("Not Accepted")