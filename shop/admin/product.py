from django.contrib import admin

from shop.models.product import Product, TagProduct, StickerProduct


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('title', 'active',
                    'sort',
                    'create_dt', 'update_dt')
    list_editable = ('active', 'sort')
    search_fields = ('title',)
    readonly_fields = ['image_tag']
    list_filter = ('active', 'create_dt', 'update_dt')


class TagProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('title', 'create_dt', 'update_dt')
    search_fields = ('title',)
    list_filter = ('create_dt', 'update_dt')


class StickerProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('title', 'image_tag', 'create_dt', 'update_dt')
    search_fields = ('title',)
    readonly_fields = ['image_tag']
    list_filter = ('create_dt', 'update_dt')


admin.site.register(Product, ProductAdmin)
admin.site.register(TagProduct, TagProductAdmin)
admin.site.register(StickerProduct, StickerProductAdmin)
