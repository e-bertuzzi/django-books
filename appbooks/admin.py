from django.contrib import admin

from .models import Book, Reading, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Reading)
admin.site.register(Author)