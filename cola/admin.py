from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category
from .models import Goods

admin.site.register(Category)
# Register your models here.




""" Django 管理サイト名変更 """
admin.site.site_header = '商品管理サイト'

""" サイト管理名変更 """
admin.site.index_title = '一覧'

class GoodsAdmin(admin.ModelAdmin):

    def good_image(self, obj):
        # 画像の存在チェック
        if obj.image:
            return mark_safe(f'<img src="{ obj.image.url }" style="width:5rem;">')
        return ''

    list_display = ('goods_name', 'good_image')
admin.site.register(Goods, GoodsAdmin)