from django.contrib import admin
from books.models import Publisher, Author, Book,User,Land,Tax

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    #fields = ('title', 'authors', 'publisher', 'publication_date')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'full_name', 'email')
    search_fields = ('user_id', 'full_name')

class TaxAdmin(admin.ModelAdmin):
    list_display = ('tax_id', 'year')


class LandAdmin(admin.ModelAdmin):
    list_display = ('land_id','catagory','area','up_for_sale')
    ordering = ('area',)
    search_fields = ('owners','land_id')
    filter_horizontal = ('owners',)


admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Tax,TaxAdmin)
admin.site.register(Land,LandAdmin)