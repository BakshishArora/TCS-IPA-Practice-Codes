import sys
sys.stdout = open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\output.txt','w')
sys.stdin = open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\input.txt','r')


class Employee:
 def __init__(self,employee_name, designation, salary ,overtimeContribution, overTimeStatus=False):
  self.employee_name = employee_name 
  self.designation= designation
  self.salary = salary 
  self.overtimeContribution = overtimeContribution
  self.overTimeStatus = overTimeStatus

class Organization:
 def __init__(self, Employee_list):
  self.Employee_list= Employee_list


 def checkEligible(self, overtimeThreshold):
    if len(self.Employee_list)==0:
        return None
    
    dic = {}
    for e in self.Employee_list:
        s = sum(e.overtimeContribution.values())
        if s >= overtimeThreshold:
            e.overTimeStatus = True 
        dic[e.employee_name]=e.overTimeStatus 

    return dic

 def CalculateBonus(self,rate):
    if len(self.Employee_list)==0:
        return None
    total_bonus = 0 
    for e in self.Employee_list:
        if e.overTimeStatus == True:
            s = sum(e.overtimeContribution.values())
            total_bonus= total_bonus + s * rate 

    return total_bonus 

n = int(input())
Employee_list = []

for i in range(n):
    employee_name = input()
    designation = input()
    salary = int(input())
    m = int(input())
    overtimeContribution= {}
    for k in range(m):
        month = input()
        hours = int(input())
        overtimeContribution[month]=hours
    Employee_list.append(Employee(employee_name,designation, salary, overtimeContribution))

o = Organization(Employee_list)
threshhold= int(input())
d = o.checkEligible(threshhold)

if d == None:
    print("No recod Found")
else:
    for k in d:
        print(k,d[k])

rate = int(input())
amount = o.CalculateBonus(rate)

if amount == 0 or amount == None:
    print("No Bonus to be paid by the Company")
else:
    print(amount)












