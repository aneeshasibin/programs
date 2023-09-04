str1="zero four zero one"
print("The Original string is:",str1)
result="".join(['0' if i=='zero' else '1' if i=='one' else '2' if i=='two' else '3'
if i=='three' else '4' if i=='four' else '5' if i=='five' else '6' if i=='six' else '7'
if i=='seven' else '8' if i=='eight' else '9' for i in str1.split()])
print(result)