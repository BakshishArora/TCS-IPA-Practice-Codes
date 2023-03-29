class Book:
    def __init__(self, pages, price,author,Id,title):
        self.pages = pages
        self.price = price 
        self.author = author 
        self.Id= Id
        self.title= title 

class BookStore:
    def __init__(self,bookStoreName,BookList):
        self.bookStoreName = bookStoreName
        self.BookList = BookList
        
    def findMinimumBookByid(self):
        if len(self.BookList) == 0: return None
        minId = 9999999
        res = None
        
        for b in self.BookList:
            if minId > b.Id:
                minId = b.Id
                res = b
        return res
    
    def sortBookById(self):
        if len(self.BookList) == 0: return None
        res = []
        for b in self.BookList:
            res.append(b.Id)
        res.sort()
        return res
        
        
n = int(input())
bookList = []
for i in range(n):
    pages = int(input())
    price = int(input())
    author=input()
    Id = int(input())
    title=input()
    bookList.append(Book(pages, price, author, Id, title))

bt = BookStore("arsh",bookList)
bk=bt.findMinimumBookByid()
if bk==None :
    print("Book Not Found")
else :
    print(bk.pages)
    print(bk.price)
    print(bk.author)
    print(bk.Id)
    print(bk.title)

iden=bt.sortBookById()
if iden==None:
    print("Book Not Found")
else:
    for k in iden:
        print(k)
        
        
'''
5
47
247 
mj demarco
19
the millionare fastlane
61
877
james clare
81
atomic habits 
90 
31
david goggins
45
can't hurt me 
24
620
youwel noa harrarie
8 
sapiens 
54
163
stephen pressfeild
97
the war of art 
'''