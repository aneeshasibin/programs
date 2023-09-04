str=input("Enter the string:")
num=len(str)
new=str[0].upper()+str[1:num-1]+str[num-1].upper()
print(new)