from django.contrib import admin
from scrapp.models import *
# Register your models here.

class cardAdmin(admin.ModelAdmin):
    list_display = ('id','pname','name','price','rating')
admin.site.register(card,cardAdmin)


class contactusAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','desc')
admin.site.register(Contact,contactusAdmin)

class SearchqueryAdmin(admin.ModelAdmin):
    list_display= ('s_query', )
admin.site.register(Search,SearchqueryAdmin)