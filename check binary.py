str1="1000101011010"
binary=['1','0']
count=0
for i in str1:
    if i in binary:
        pass
    else:
        count+=1
if count==0:
    print("The given string is binary")
else:
    print("The given string is not a binary")