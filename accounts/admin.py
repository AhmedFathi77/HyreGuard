from django.contrib import admin
from .models import CreateUser

# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('FirstName', 'Email', 'Country', 'Acc_Type')

admin.site.register(CreateUser)