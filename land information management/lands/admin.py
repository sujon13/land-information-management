

from django.contrib import admin
from lands.models import User,Land,Tax


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'full_name', 'email')
    search_fields = ('user_id', 'full_name')

class TaxAdmin(admin.ModelAdmin):
    list_display = ('tax_id', 'year')




class LandAdmin(admin.ModelAdmin):
    list_display = ('land_id','catagory','area','up_for_sale')
    ordering = ('area',)
    search_fields = ('owners','land_id')





admin.site.register(User,UserAdmin)
admin.site.register(Tax,TaxAdmin)
admin.site.register(Land,LandAdmin)
