from django.contrib import admin
from .models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdminModel(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'car_title', 'city', 'created_date']
    list_display_link = ['id', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'email', 'car_title']
    list_per_page = 25


