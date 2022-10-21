class Library:
  def _init_(self,books):
    self.books=books

  def list_books(self):
    print("avaialable books")
    for book in self.books:
      print(book)
  def borrowed_book(self,borrow_book):
    if borrow_book in self.books:
      print("get your book now")
      self.books.remove(borrow_book)
    else:
      print("book not available")
  def receive_book(self,receive_book):
    print("you have returned the book")
    self.books.append(receive_book)
books=['python','c','c++','html','java','numpy','pandas']
O=Library(books)
class Li:
  def _init_(self,newspaper):
    self.newspaper=newspaper

  def list_newspaper(self):
    print("available newpaper")
    for paper in self.newspaper:
      print(paper)
  def borrowed_newspaper(self,borrow_newpaper):
    if borrow_newpaper in self.newspaper:
      print("we cant give borrow a newpaper it is only for reading purpose")
    else:
      print("you are searching np is not available and also cant give  borrow a np it is only for reading")
newspaper=['hindu','dc',"times of india",'the week']

a=Li(newspaper)
class L:
  def _init_(self,journals):
    self.journals=journals

  def list_journals(self):
    print("avalaiable journals are :")
    for journals in self.journals:
      print(journals)
  def borrow_journal(self,borrow_journal):
    if borrow_journal in self.journals:
      print("get your journal")
      self.journals.remove(journal)
    else:
      print("journal not available")
  def receive_journal(self,receive_journal):
      print("you have returned the journal")
      self.journals.append(journal)



journals=["IEEE",'Google Scholar',"Grammarly","IET"]
g=L(journals)
class Ebooks:
  def _init_(self,ebooks):
    self.ebooks=ebooks

  def list_ebooks(self):
    print("available ebooks")
    for ebook in self.ebooks:
      print(ebook)
  def borrow_ebook(self,borrow_ebook):
    if borrow_ebook in self.ebooks:
      print("get your book now")
      self.ebooks.remove(borrow_ebook)
    else:
      print("ebook is not available")

  def receive_ebook(self,receive_ebook):
    print("you have return the ebook")
    self.ebooks.append(receive_ebook)

ebooks=["Apple iPad","Sony Reader","Barnes & Noble Nook and Nook Tablet","Amazon Kindle and Fire tablets"]
x=Ebooks(ebooks)
msg="""
    1.display books
    2.borrow book
    3.return book
    4.display newspaper
    5.borrow newspaper
    6.list_journals
    7.borrow_journals
    8.return journals
    9.list_ebooks
    10.borrow_ebooks
    11.return_ebooks"""
while True:
  print(msg)
  ch=int(input())
  if ch==1:
    O.list_books()
  elif ch==2:
    books=input("Enter book name to borrow")
    O.borrowed_book(books)
  elif ch==3:
    books=input("enter book name to return ")
    O.receive_book(books)
  elif ch==4:
    a.list_newspaper()
  elif ch==5:
    newspaper=input("enter newspaper name")
    a.borrowed_newspaper(newspaper)
  elif ch==6:
    g.list_journals()
  elif ch==7:
    journal=input("enter your journal name:")
    g.borrow_journal(journal)
  elif ch==8:
    journal=input("enter your journal name:")
    g.receive_journal(journal)
  elif ch==9:
    x.list_ebooks()
  elif ch==10:
    ebook=input("enter your ebook name:")
    x.borrow_ebook(ebook)
  elif ch==11:
    ebook=input("enter your ebook name :")
    x.receive_ebook(ebook)
  else:
    print("Thank you come again")
    quit()
