import sys 
sys.stdout= open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\output.txt','w')
sys.stdin = open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\input.txt','r')

class Employee:
 def __init__(self,name,designation,salary,loandetail):
  self.name= name
  self.designation= designation
  self.salary= salary
  self.loandetails= loandetails

class Organization:
 def __init__(self,employeeList,loantypes,dwiseloan):
  self.employeeList= employeeList
  self.loantypes= loantypes 
  self.dwiseloan= dwiseloan

 def checkeligible(self,nameg,loantypeg,amountg):
  if len(employeeList)==0:
   return False  

  for i in self.employeeList:
   if(i.name == nameg):
    if loantypeg not in i.loandetails.keys():
     if loantypeg in self.loantypes:
      borrow = amountg + sum(i.loandetails.values())
      if i.designation in self.dwiseloan.keys():
       if(borrow <= self.dwiseloan[i.designation]):
         i.loandetails[loantypeg]= amountg
         return i.loandetails

  return False

 def count(self):
  if len(self.employeeList)==0:
   return None
  dic = {}
  for i in self.employeeList:
   borrow = sum(i.loandetails.values())
   if i.designation in self.dwiseloan.keys():
    if borrow < self.dwiseloan[i.designation]:
     if i.designation not in dic:
      dic[i.designation]=1
     else:
      dic[i.designation]=dic[i.designation]+1
    else:
     dic[i.designation]=0 
  if len(dic)==0:
   return None 
  else:
   dic = dict(sorted(dic.items(), key = lambda x : x[0], reverse= True ))
   return dic
   
  

if __name__=='__main__':
 n = int(input())
 employeeList = []
 for i in range(n):
  name = input().lower()
  designation= input().lower()
  salary = int(input())
  m = int(input())
  loandetails={}
  for k in range(m):
   type= input().lower()
   amt = int(input())
   loandetails[type]=amt
  employeeList.append(Employee(name,designation,salary,loandetails)) 

 typelist = []
 t = int(input())
 for i in range(t):
  typelist.append(input().lower())

 dwiseloandic={}
 k = int(input())
 for i in range(k):
  desig = input().lower()
  amnt = int(input())
  dwiseloandic[desig]= amnt

 nameg = input().lower()
 typeg = input().lower()
 amtg=int(input())
 
 o = Organization(employeeList,typelist,dwiseloandic)
 ans1 = o.checkeligible(nameg,typeg,amtg)
 if ans1 == 'False' or len(ans1)==0:
  print('Loan Not Granted')
 else:
  print('Loan Granted')
  for k in ans1:
   print(k.capitalize() + " : " + str(ans1[k]))

 ans2 = o.count()

 if ans2 == None:
  print('No record Found')
 else:
  for i in ans2:
   print(i.capitalize() + " : " + str(ans2[i])) 