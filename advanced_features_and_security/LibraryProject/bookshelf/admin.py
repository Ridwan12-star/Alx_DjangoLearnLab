from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Shows these fields in the admin list view
    search_fields = ('title', 'author')                     # Enables search by title and author
    list_filter = ('publication_year',)                     # Adds a filter by year on the side

from django.contrib import admin
from .models import Book

admin.site.register(Book)
