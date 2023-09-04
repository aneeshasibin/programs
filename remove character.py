string=input("Enter the string:")
new=[]
for j in string:
    if j=='i':
        continue
    else:
        new.append(j)
print("".join(new))