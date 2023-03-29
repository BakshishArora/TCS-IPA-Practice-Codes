import sys 
sys.stdout = open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\input.txt','w')
sys.stdin = open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\output.txt','r')

class Apparel:
 def __init__(self,brand,ptype,price,avail):
  self.brand= brand
  self.ptype = ptype 
  self.price = price 
  self.avail= avail 


class Store:
 def __init__(self,apparel_list):
  self.apparel_list= apparel_list 

 def check(self,brandg,typeg,sizeg,quantity):
  if len(self.apparel_list)==0:
   return None

  for i in self.apparel_list:
   if i.brand == brandg and i.type == typeg:
    flag=1 
    for j in i.avail.items():
     if j==sizeg and i.avail[j]>=quantity:
      i.avail[sizeg]-=quantity
      return True
  return False     
    


if __name__=='__main__':
 
 n= int(input())
 apparel_list =[]
 for i in range(n):
  brand = input()
  ptype = input()
  price = int(input())
  avail={}
  for k in range(n):
   size= input().upper()
   quantity = int(input())
   avail[size]=quantity 
  apparel_list.append(Apparel(brand,ptype,price,avail))

 s= Store(apparel_list)
 brandg= input()
 typeg= input()
 sizeg= input()
 quantity= int(input())

 ans = s.check(brandg,typeg,sizeg,quantity)
 if ans == True:
  print("Size is available")
 else:
  print("Size is not available")
 
 flag=0
 for i in apparel_list:
  if i.brand == brandg and i.type == typeg:
   flag = 1
   for k in i.avail.items():
    print(k,":".str(i.avail[k]))

 if flag == 0:
  print('Apparel not found')
    