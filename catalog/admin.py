from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('book', 'status')
    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'inv_nom')}),
        ('Availability', {'fields': ('status', 'due_back', 'borrower')})
    )
