from django.contrib import admin
from .models import User, Post, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'is_superuser')
    list_filter = ('is_active', 'is_superuser', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'content_preview')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content', 'author__first_name', 'author__last_name')
    inlines = [CommentInLine]
    ordering = ('created_at',)

    def content_preview(self, obj):
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content

    content_preview.short_description = 'Content Preview'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_preview', 'author', 'post', 'created_at')
    list_filter = ('author', 'post', 'created_at')
    search_fields = ('content', 'author__first_name', 'author__last_name', 'post__title')
    ordering = ('post', 'created_at',)

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    content_preview.short_description = 'Content Preview'
