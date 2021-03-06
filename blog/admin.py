from django.contrib import admin
from blog.models import Category, Tag, Post, Contact
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('status', 'tags')
    list_display = ('title', 'status', 'publication_date', 'category', 'author')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, BlogAdmin)
admin.site.register(Contact)