from django.contrib import admin
from .models import Post, Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'categories', 'deleted']
    search_fields = ['title', 'sub_title']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
