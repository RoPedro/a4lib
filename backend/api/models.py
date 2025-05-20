from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_author')
        ]
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    published_date = models.DateField()
    is_hidden = models.BooleanField(default=True) # Simula um embargo, cadastrado mas não visível para usuários.
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title

# Cópias de um livro
class BookUnit(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    unit_number = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book.title} - Unit {self.unit_number}"

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Empréstimo de um livro 
class Borrow(models.Model):
    book_unit = models.ForeignKey(BookUnit, on_delete=models.CASCADE)
    borrower_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.borrower_name} borrowed {self.book_unit.book.title} - Unit {self.book_unit.unit_number}"