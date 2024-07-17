from django.contrib import admin
from .models import Book

# admin page customization 
class BookAdmin(admin.ModelAdmin):
  list_display = ("author","title","description","rating","publish_date")
# Register your models here.

admin.site.register(Book,BookAdmin)


