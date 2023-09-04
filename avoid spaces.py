def avoid(str):
    new=[]
    for i in str:
        if i==" ":
            continue
        else:
            new.append(i)
    print("".join(new))
str='Hello World'
avoid(str)