from django.contrib import admin

from shop.models.product import Product, TagProduct, StickerProduct


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('title', 'active', 'category', 'image_tag', 'price', 'price_procurement',
                    'tag', 'sticker', 'sort', 'create_dt', 'update_dt')
    list_editable = ('active', 'sort', 'sticker')
    search_fields = ('title',)
    readonly_fields = ['image_tag']
    list_filter = ('active', 'category', 'tag', 'sticker', 'create_dt', 'update_dt')


class TagProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('title', 'url', 'create_dt', 'update_dt')
    search_fields = ('title',)
    list_filter = ('create_dt', 'update_dt')


class StickerProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('title', 'url', 'image_tag', 'create_dt', 'update_dt')
    search_fields = ('title',)
    readonly_fields = ['image_tag']
    list_filter = ('create_dt', 'update_dt')


admin.site.register(Product, ProductAdmin)
admin.site.register(TagProduct, TagProductAdmin)
admin.site.register(StickerProduct, StickerProductAdmin)
