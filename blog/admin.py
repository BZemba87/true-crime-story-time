from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', )
    search = ['title', 'content']


admin.site.register(Post, PostAdmin)

# Register your models here.
