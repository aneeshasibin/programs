str1="keep coding"
str2="keep coding it will make you perfect"
str1=str1.split()
str2=str2.split()
x=[]
for i in str1:
    if i not in str2:
        x.append(i)
for i in str2:
    if i not in str1:
        x.append(i)
print(x)

