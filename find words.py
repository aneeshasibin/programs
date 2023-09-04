str1="helloworld is every progammers first program"
print("The original string is:",str(str1))
new=str1.split()
k=5

for i in new:
    if len(i)>k:
        print(i)