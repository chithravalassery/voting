from django.contrib import admin
from .models import Book, Author
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=[ 'title', 'author', 'price']
    ordering=('-title',)

admin.site.register(Book,BookAdmin)
admin.site.register(Author)

