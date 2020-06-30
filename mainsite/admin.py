from django.contrib import admin
from .models import Post
from mainsite import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)

class MoodPostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'enabled', 'pub_time')
    ordering = ('-pub_time',)
admin.site.register(models.Mood)
admin.site.register(models.MoodPost, MoodPostAdmin)