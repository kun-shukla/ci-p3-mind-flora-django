from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, UserRecommendedDestination

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('category', 'title', 'slug', 'status','created_on')
    search_fields = ['title','content']
    list_filter = ('status','category','created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(UserRecommendedDestination)
class UserRecommendedDestinationAdmin(admin.ModelAdmin):

    list_display = ('destination', 'read',)

# Register your models here.
admin.site.register(Comment)
