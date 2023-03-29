import sys 
sys.stdout= open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\output.txt','w')
sys.stdin= open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\input.txt','r')


def check_palindrome(string):
 l = len(string)
 
 for i in range(len(string)//2):
   if(i<=l):
    #print(i,l-1)
    if string[i]==string[l-1]:
     i = i + 1
     l = l-1
    else:
     return False
 return True 


if __name__=='__main__':
 n = int(input())
 lis =[]
 for i in range(n):
  string = input()
  lis.append(string)


 for i in lis:
  if (check_palindrome(i)):
   print(i)