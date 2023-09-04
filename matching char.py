def matchchar(str1,str2):
    return len(set(str1).intersection(set(str2)))
str1=input("Enter the 1st string:")
str2=input("Enter the 2nd string:")
num=matchchar(str1.lower(),str2.lower())
print("The number of matching characters is ",num)