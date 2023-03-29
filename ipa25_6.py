import sys 
sys.stdout= open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\output.txt','w')
sys.stdin= open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\input.txt','r')

class Service:
 def __init__(self,serviceId,regNo,model,mileage,isInsured,paymentRecvd):
  self.serviceId = serviceId
  self.regNo = regNo
  self.model = model
  self.mileage = mileage 
  self.isInsured = isInsured 
  self.paymentRecvd = paymentRecvd


class ServiceCenter:
 def __init__(self,mileagedict,serviceList):
  self.mileagedict = mileagedict
  self.serviceList = serviceList 

 def getTotalPaymentOfInsuredCars(self,manufacturername , statecode):
  if len(self.serviceList)==0:
   return None 
  total_payment = 0 
  for i in self.serviceList: 
   if i.isInsured=='yes':
    if manufacturername in i.model.split():
     if statecode in i.regNo:
      total_payment += i.payementRecvd
  if total_payment ==0:
   return None
  else:
   return total_payment
 
 def getServicedCarWithProperMileage(self):
  if len(self.serviceList)==0:
   return None
  
  if len(self.mileagedict)==0:
   return None
  lis =[]
  for i in self.serviceList:
   if i.model in self.mileagedict.keys():
    if i.mileage >= self.mileagedict[i.model]:
     lis.append(i)
     #lis = sorted(lis, key = lambda x : x [3], reverse = True )

  if len(lis)==0:
   return None 
  else:
   #lis = sorted(lis, key = lambda x : x ['mileage'], reverse = True )
   return lis 
  
if __name__=='__main__':
 n = int(input())
 serviceList =[]
 for i in range(n):
  serviceId = int(input())
  regNo= input().lower()
  model = input().lower()
  mileage = int(input())
  isInsured = input().lower()
  paymentRecvd = int(input())
  serviceList.append(Service(serviceId, regNo, model,mileage , isInsured , paymentRecvd))
 mileagedict = {}
 m = int(input())
 for i in range(m):
  k = input().lower()
  v = int(input())
  mileagedict[k]=v

 nameg = input().lower()
 codeg= input().lower()

 s = ServiceCenter(mileagedict,serviceList)
 ans1 = s.getTotalPaymentOfInsuredCars(nameg,codeg)
 if ans1 == None:
  print('Insured car not found with given model and state')
 else:
  print(codeg.upper(), nameg.upper(), ans1)

 ans2 = s.getServicedCarWithProperMileage()
 if ans2 == None:
  print('car not found')
 else:
  for i in ans2:
   print(str(i.serviceId)+' # '+i.regNo.upper() +' # '+ i.model.capitalize()+' # '+str(i.mileage))
   



     
    