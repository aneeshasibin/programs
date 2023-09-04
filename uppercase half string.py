str=input("Enter the string:")
num=len(str)//2
newstring=str[:num].upper()+str[num:]
print(newstring)