from operator import attrgetter

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
        res = min(self.BookList,key=attrgetter('Id'))
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
        
        

    
    
    