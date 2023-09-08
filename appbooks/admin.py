from django.contrib import admin

from .models import Book, Reading, Author, Quote

# Register your models here.
admin.site.register(Book)
admin.site.register(Reading)
admin.site.register(Author)
admin.site.register(Quote)