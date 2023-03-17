class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"{self.title} by {self.author}"
        
    def __len__(self):
        return self.pages

mybook = Book('Python Rocks','Jose',250)

length_book = len(mybook)

print(mybook)
print(length_book)
