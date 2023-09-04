str1="helloworld"
print("The original string is",str1)
str2={}
for i in str1:
    if i in str2:
        str2[i]+=1
    else:
        str2[i]=1
res=min(str2,key=str2.get)
print("The minimum of all characters in ",str1,"is :",res)