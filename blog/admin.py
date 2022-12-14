from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', )
    summernote_fields = ('content')
    search = ['title', 'content']


admin.site.register(Post, PostAdmin)

# Register your models here.
