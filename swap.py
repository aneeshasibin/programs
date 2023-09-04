str1="hello,world."
new=[]
for i in str1:
    if i==',':
       new.append('.')
    elif i=='.':
        new.append(',')
    else:
        new.append(i)
print("".join(new))