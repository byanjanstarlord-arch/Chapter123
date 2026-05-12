from django.contrib import admin
from django.utils.html import format_html
from .models import Post
from .models import Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status', 'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active', 'publish']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS
    actions = ['make_active', 'make_inactive']

    @admin.action(description='Mark selected posts as active')
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description='Mark selected posts as inactive')
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    @admin.display(description='Status')
    def status(self, obj):
        if obj.is_active:
            return format_html(
                '<span style="color: #1f7a3a; font-weight: 600;">Active</span>'
            )
        return format_html(
            '<span style="color: #b42318; font-weight: 600;">Inactive</span>'
        )



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','created','active']
    list_filter = ['active','created','updated']
    search_fields = ['name','email','body']
