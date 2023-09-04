str1="our aim of life should be is to be happy"
print("The original string is :",str1)
l=str1.split()
new=[]
for i in l:
    if len(i)%2!=0:
        new.append(i)
print(" ".join(new))