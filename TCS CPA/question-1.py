class Player:
    def __init__(self,playerName, team, playerType, isCaptain, runs, wickets):
        self.playerName= playerName
        self.team=team
        self.playerType= playerType
        self.isCaptain=isCaptain
        self.runs=runs
        self.wickets=wickets 
    
    def calculatePoints(self):
        if(self.isCaptain == "True"):
            points = 2*(self.runs + 10*self.wickets) 
        else:
            points = self.runs + 10*self.wickets
        return points
    

class Tournament:
    
    def __init__(self,PlayerList):
        self.PlayerList=PlayerList
         
    def getPlayerlist(self,playerType, points):
        result = []
        for p in self.PlayerList:
            Pt= p.playerType  
            pts= p.calculatePoints()
            
            if(Pt.lower()==playerType.lower() and pts > points):
                result.append(p)
                
        if len(result)==0:
            result=None
            
        return result
            
    
    def findPlayerPoints(self,team, points):
        dit = {}
        for i in self.PlayerList:
            if(i.team.lower() == team.lower() and i.calculatePoints()>points):
                   dit[i.playerName]=i.calculatePoints()
        if len(dit)==0:
            dit = None
            
        return dit
            
        
        
n = int(input())
playerList=[]

for p in range(n):
    playerName = input()
    team = input()
    playerType=input()
    isCaptain = input()
    runs = int(input())
    wickets = int(input())
    playerList.append(Player(playerName, team, playerType, isCaptain,runs,wickets))

t = Tournament(playerList)

res= t.getPlayerlist(input(),int(input()))
if res==None:
    print("Player Not Found")
else:
    for i in res:
        print(i.playerName)
        print(i.runs)
        print(i.wickets)

f=t.findPlayerPoints(input(),int(input()))
if f == None:
    print("Player Not Found")
else:
    for k in f:
        print(k, f[k])



'''
5
virat
rcb
batter
True
410
0
bumrah
mi
baller
False
50
25
maxwell
rcb
allrounder
False
350
6
hardik
mi
allrounder
False
300
2
chahal
rcb
baller
False
30
23
Allrounder
250
RCB
350
'''