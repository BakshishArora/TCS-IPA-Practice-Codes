def find_index(lis,string):
    for i in range(len(lis)):
        if lis[i]==string:
            return i 
       

n = int(input())
lis=[]
for i in range(n):
    lis.append(input())
string = input()

t=find_index(lis,string)
if(t == None):
    print("string not found in the list")
else:
    print(t)