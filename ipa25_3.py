import sys 
sys.stdout= open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\output.txt','w')
sys.stdin = open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\input.txt','r')

class Painting:
 def __init__(self,paintingId,painterName,paintingPrice,paintingType):
  self.paintingId = paintingId
  self.painterName = painterName 
  self.paintingPrice = paintingPrice 
  self.paintingType = paintingType 

class ShowRoom:
 def __init__(self,paintingList):
  self.paintingList = paintingList 

 def getTotalPaintingPrice(self,typeg):
  if len(self.paintingList)==0:
   return None

  total_price = 0

  for i in self.paintingList:
   if i.paintingType.lower() == typeg.lower():
    total_price += i.paintingPrice

  if total_price == 0:
   return None
  else:
   return total_price


 def getPainterWithMaxCountOfPaintings(self):
 
  if len(self.paintingList)==0:
   return None

  count =0 
  dic = {}

  for i in self.paintingList:
   if i.painterName not in dic:
    dic[i.painterName]=1
   else:
    dic[i.painterName]= dic[i.painterName]+1

  dic =sorted(dic.items(), key = lambda x: x[1], reverse = True)
  lis = []
  p = dic[0][1]
  for k in range(len(dic)):
   if p == dic[k][1]:
    lis.append(dic[k][0])

  lis = sorted(lis)
  return lis[0]

   
  return lis[0] 


if __name__=='__main__':
 n = int(input())
 paintingList = []
 
 for i in range(n):
  painterId = int(input())
  painterName = input().lower()
  paintingPrice = int(input())
  paintingType = input()
  paintingList.append(Painting(painterId,painterName,paintingPrice,paintingType))

 s = ShowRoom(paintingList)
 typeg = input()

 total_price = s.getTotalPaintingPrice(typeg)
 if total_price == None:
  print('No painting found')
 else:
  print(total_price)

 dic = s.getPainterWithMaxCountOfPaintings()
 if dic == None:
  print('No Painter Found')
 else:
  print(dic.capitalize())