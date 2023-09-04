str1="hello"
print("The original string is:",str1)
newstr=[]
for i in str1:
    if str1.count(i)%2!=0:
        newstr.append(i)
print("The odd frequency characters is:",str(newstr))