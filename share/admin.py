from django.contrib import admin
from share.models import Account, Blog,Diary,Travel_plan
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('Username',)
    search_fields = ('Username',)
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('Title',)

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('Title',)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('Username',)
    
admin.site.register(Account,AccountAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Diary,DiaryAdmin)
admin.site.register(Travel_plan,PlanAdmin)
