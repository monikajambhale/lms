class Library:
    def __init__(self,booklist):
        self.books=booklist

    def showAvailableBooks(self):
        print("The available books are:")
        for item in self.books:
            print("-"+item)

    def borrowBook(self,borrow):
        if(borrow in self.books):
            print("You have been issued "+borrow+". Please return it after 30 days.\nThank you!")
            self.books.remove(borrow)
            return True
        else:
            print(borrow+" is not available right now.\nPlease check back later.")
            return False

    def returnBook(self,returnbook):
        if(returnbook not in self.books):
            self.books.append(returnbook)
            print("Thank you for the book!")
        elif(returnbook==" "):
            print("Please enter the book name.")
        else:
            print("Sorry the library already has "+returnbook+"..")

class Student:
    def requestBook(self):
        self.book=input("Enter the book you want to borrow: ")
        return self.book
    
    def returnBook(self):
        self.book=input("Enter the book you want to return/donate: ")
        return self.book

lib=Library(["Python","Java","Harry Potter","C++","C"])
stud=Student()
while(True):
    welcome='''*****Welcome to the Library*****
    Please choose one of the following:
    1: Check out all the available books.
    2: Request a book.
    3: Return/donate a book.
    4: Exit.'''
    print(welcome)
    ch=int(input("Enter an option: "))
    if(ch==1):
        lib.showAvailableBooks()
    elif(ch==2):
        lib.borrowBook(stud.requestBook())
    elif(ch==3):
        lib.returnBook(stud.returnBook())
    elif(ch==4):
        print("Thank you for using this library:) Hope to see you soon.")
        break
    else:
        print("Invalid option")
        