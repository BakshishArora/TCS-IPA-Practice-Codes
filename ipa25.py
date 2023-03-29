import sys
sys.stdout = open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\output.txt','w') 
sys.stdin = open('C:\\Users\\baksh\\Desktop\\DSA\\TCS IPA\\input.txt','r')

class Player:
 def __init__(self,name, country,age,matches,runs, wickets):
  self.name= name 
  self.country=country
  self.age=age
  self.matches = matches 
  self.runs = runs 
  self.wickets = wickets 

class Team:
 def __init__(self,playerlist):
  self.playerlist = playerlist 

 def minruns(self):
  min = self.playerlist[0]
  for i in self.playerlist:
   if i.runs < min.runs:
    min = i 
  return min 

 def wickets(self):
  max = self.playerlist[0]
  for i in self.playerlist:
   if i.wickets > max.wickets:
    max = i
  return max


if __name__=='__main__':
 
 n = int(input())
 playerlist =[]

 for i in range(n):
  name = input()
  country = input()
  age= int(input())
  matches = int(input())
  runs = int(input())
  wickets = int(input())
  playerlist.append(Player(name,country,age,matches,runs,wickets))

 t = Team(playerlist)

 min_runs = t.minruns()
 print(min_runs.name)
 print(min_runs.runs)
 print(min_runs.country)

 max_wickets = t.wickets()
 print(max_wickets.name)
 print(max_wickets.wickets)
 print(max_wickets.country)

 