class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.available = True

  def borrow(self):
    if self.available:
      self.available = False
      print(f"O livro {self.title} já foi emprestado")
    else:
      print(f"O livro {self.title} não está disponível")

  def return_book(self):
      self.available = True
      print(f"O livro {self.title} foi devolvido")

class User:
  def __init__(self, name, user_id):
    self.name = name
    self.user_id = user_id
    self.borrowed_books = []

  def borrow_book(self, book):
    if book.available:
      book.borrow()
      self.borrowed_books.append(book)
    else:
      print(f"O livro {book.title} não está disponível")

  def return_book(self, book):
    if book in self.borrowed_books:
      book.return_book()
      self.borrowed_books.remove(book)
    else:
      print(f"O livro {book.title} não está na lista de empréstimos")
  
class Library:
  def __init__(self):
    self.books = []
    self.users = []
    
  def add_book(self, book):
    self.books.append(book)
    print(f"O livro {book.title} foi adicionado com sucesso")

  def register_user(self, user):
    self.users.append(user)
    print(f"O usuário {user.name} foi registrado com sucesso")

  def show_available_books(self):
    print(f"Livros disponíveis:")
    for book in self.books:
      if book.available:
        print(f"{book.title} por {book.author}")

# Criar os livros
book1 = Book("Primeiro Milhão", "Raiam Santos")
book2 = Book("Quem Pensa Enriquece", "Napoleon Hill")

# Criar um usuário
user1 = User("Jair Raya", "001")

# Criar biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

# Mostrar livros
library.show_available_books()

# Realizar emprétimo
user1.borrow_book(book1)

# Mostrar livros
library.show_available_books()

# Devolver livro
user1.return_book(book1)

# Mostrar livros
library.show_available_books()