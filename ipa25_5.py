import sys 
sys.stdout= open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\output.txt','w')
sys.stdin= open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\input.txt','r')

class Student:
 def __init__(self,roll,name,marks):
  self.roll = roll
  self.name = name
  self.marks = marks

 def calculate_percentage(self):
  m = len(self.marks)
  percentage = sum(self.marks)/m
  return int(percentage)

 def find_grade(self):
  m = len(self.marks)
  percentage = int(sum(self.marks)/m)
  grade = ['A','B','C','F']
  if percentage >= 80:
   gradeout = grade[0]
  elif 60 <= percentage < 80:
   gradeout = grade[1]
  elif 40<=percentage<60:
   gradeout = grade[2]
  else:
   gradeout = grade[3]
    
  return gradeout 


if __name__=='__main__':
 #n = int(input())
 
 roll = int(input())
 name = input()
 m = int(input())
 marks = []
 for i in range(m):
  marks.append(int(input()))
 s = Student(roll,name,marks)
 per = s.calculate_percentage()
 print(per)
 grade = s.find_grade()
 print(grade)
 