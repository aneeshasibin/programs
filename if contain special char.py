str1="helloworld@123*"
special=['!','@','#','$','%','^','&','*','()','_','-','+','=','<','>','?','/']
new=[]
for i in str1:
    if i in special:
       new.append(i)
print("Special characters is:",str(new))