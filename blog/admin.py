from django.contrib import admin
from blog.models import Tag, Post

# Register your models here.
# Tag is directly used
admin.site.register(Tag)

# While Post has a custom admin class

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title', )}
    list_display = ['title', 'published_at', 'slug']


admin.site.register(Post, PostAdmin)
