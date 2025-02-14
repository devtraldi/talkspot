from django.contrib import admin
from .models import User, Post, Comment, Quote


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'email', 'is_active', 'date_joined', 'is_superuser')
    list_filter = ('is_active', 'is_superuser', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'content_preview', 'total_likes_display')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content', 'author__first_name', 'author__last_name')
    inlines = [CommentInLine]
    ordering = ('created_at',)

    def content_preview(self, obj):
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content

    content_preview.short_description = 'Content Preview'

    def total_likes_display(self, obj):
        return obj.total_likes()

    total_likes_display.short_description = 'Total Likes'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_preview', 'author', 'post', 'created_at')
    list_filter = ('author', 'post', 'created_at')
    search_fields = ('content', 'author__first_name', 'author__last_name', 'post__title')
    ordering = ('post', 'created_at',)

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    content_preview.short_description = 'Content Preview'


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    # Campos exibidos na lista de citações
    list_display = ('content_preview', 'character')  # Removi 'created_at'

    # Filtros laterais (agora como uma lista)
    list_filter = ('character',)  # Adicione uma vírgula para transformar em tupla

    # Campos de pesquisa
    search_fields = ('text', 'character')

    # Ordenação padrão
    ordering = ('character',)  # Ordena por personagem

    # Função para reduzir a quantidade de caracteres exibidos
    def content_preview(self, obj):
        return obj.text[:100] + '...' if len(obj.text) > 100 else obj.text

    content_preview.short_description = 'Quote Preview'  # Nome da coluna na lista