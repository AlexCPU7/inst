from django.contrib import admin
from shop.models.catalog import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('title', 'active', 'parent_category', 'image_tag', 'sort',
                    'create_dt', 'update_dt')
    list_editable = ('active', 'parent_category', 'sort')
    search_fields = ('title',)
    readonly_fields = ['image_tag']
    # readonly_fields = ('image',)
    list_filter = ('active', 'create_dt', 'update_dt')


admin.site.register(Category, CategoryAdmin)
