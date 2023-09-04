str1="helloo woorlld"
print("The original string is:",str1)
res=[]
count=1
for i in range(len(str1)-1):
    if str1[i]==str1[i+1]:
        count+=1
    else:
        res.append(count)
        count=1
res.append(count)  
print("The consicutive characters frequency is",str(res))