import sys 
sys.stdout = open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\output.txt','w')
sys.stdin = open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\input.txt','r')

def check(string1, string2):
 count = []
 for i in string1:
  for j in string2:
   if i==j:
    count.append(True)
  count.append(False)
 
 if 'False' in count:
  return False 
 else:
  return True  
 

if __name__=='__main__':

 string1 = input()
 string2 = input()

 if(check(string1, string2)== True):
  print("Input string is valid")
 else:
  print("Input string is not valid")