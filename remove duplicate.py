def removedup(str):
    t=""
    for i in str:
        if i in t:
            pass
        else:
            t=t+i
    print(t)
str='helloworld'
removedup(str)