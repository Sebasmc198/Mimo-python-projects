class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.available = True

  def checkout(self):
    if self.available:
      self.available = False
      return True
    else:
      return False
  
  def return_book(self):
    self.available = True

  def display_info(self):
    print(f"Title: {self.title}.\nAuthor: {self.author}.\nAvailable?: {self.available}")

book1 = Book("Don Quijote de la Mancha", "Miguel de Cervantes")
book2 = Book("Buscando a Alaska", "John Green")
book3 = Book("El Gran Gatsby", "F. Scott Fitzgerald")

books = (book1, book2, book3)

for book in books:
  book.display_info()