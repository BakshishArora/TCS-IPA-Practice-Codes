def check(string):
    flag = True
    for i in range(0,len(string)):
        if string[i].isalpha() or string[i]==" ":
            continue
        else:
            flag = False
            break 
    return flag
            
n = int(input())
lis=[]
valid = 0 
invalid = 0

for i in range(n):
    lis.append(input())
    
for k in lis:
    if(check(k)):
        valid+=1
    else:
        invalid+=1
        
print("The valid string : {}".format(valid))
print("The invalid string : {}".format(invalid))

'''
5
ABCDefg hij
abc123@
proctored.c
abcde fgh
avcdf345f
'''