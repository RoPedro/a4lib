from django.contrib import admin

from .models import Book, Author, Genre, User, Borrow, BookUnit

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(User)
admin.site.register(Borrow)
admin.site.register(BookUnit)