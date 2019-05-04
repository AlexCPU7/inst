from django.contrib import admin
from core.models.news.news import News
from core.models.news.attribute_news import NewsCategory, NewsTag


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('title', 'active', 'author', 'preview_image_tag', 'view', 'sort',
                    'create_dt', 'update_dt')
    list_editable = ('active', 'sort')
    search_fields = ('title', 'view')
    readonly_fields = ('preview_image_tag', 'image_tag')
    list_filter = ('active', 'create_dt', 'update_dt')


class NewsCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('title', 'active', 'sort', 'create_dt', 'update_dt')
    list_editable = ('active', 'sort')
    search_fields = ('title',)
    readonly_fields = ('image_tag',)
    list_filter = ('active', 'create_dt', 'update_dt')


class NewsTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('title', 'active', 'create_dt', 'update_dt')
    list_editable = ('active',)
    search_fields = ('title',)
    list_filter = ('active', 'create_dt', 'update_dt')


admin.site.register(News, NewsAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(NewsTag, NewsTagAdmin)
