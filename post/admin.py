from django.contrib import admin
from post.models import Post, Tag, Follow, Stream

# Register your models here.
admin.site.register(Tag)
admin.site.register(Follow)
admin.site.register(Stream)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id","picture", "user","happy","surprise")