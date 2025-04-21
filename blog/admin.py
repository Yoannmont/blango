from django.contrib import admin
from blog.models import Tag, Post, Comment, AuthorProfile

# Register your models here.
# Tag is directly used
admin.site.register(Tag)
admin.site.register(AuthorProfile)

# While Post has a custom admin class


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title', )}
    list_display = ['title', 'published_at', 'slug']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'object_id',)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Post, PostAdmin)
