from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    list_filter = ["title", "author"]
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ["slug"]

admin.site.register(Book, BookAdmin)