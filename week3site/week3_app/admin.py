from django.contrib import admin

# Register your models here.
from week3_app.models import Author
from week3_app.models import Book
from week3_app.models import Publisher

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
