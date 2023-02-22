from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User



from .models import user,categry,subcategory,expert_tbl,question,Pending,tbl_answer,tbl_chat



class adminuser(admin.ModelAdmin):
    list_display = ['f_name', 'l_name', 'mobile', 'email', 'gender']
    list_per_page = 10

class adminexpert_tbl(admin.ModelAdmin):
     list_display = ['f_name', 'cat', 'mobile',  'interest','email']
     list_per_page = 10

     class adminquestion(admin.ModelAdmin):
         list_display = ['f_name']


# Register your models here.

admin.site.register(user, adminuser)
admin.site.register(expert_tbl,adminexpert_tbl)
admin.site.register(categry)
admin.site.register(tbl_answer)
admin.site.register(Pending)
admin.site.register(subcategory)
admin.site.register(question)
admin.site.register(tbl_chat)

admin.site.unregister(Group)

admin.site.unregister(User)

