str1="helloworld"
i=5
l=[]
for j in range(len(str1)):
    if j==i:
        continue
    else:
        l.append(str1[j])
print("".join(l))
