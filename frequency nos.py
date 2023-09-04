str1="helloworld 123"
count=0
for i in str1:
    if i.isdigit():
        count+=1
print("Frequency of numbers in string:",count)        