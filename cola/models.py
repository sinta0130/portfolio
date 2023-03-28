from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = "カテゴリテーブル"
        verbose_name_plural = "カテゴリテーブル"

class Goods(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    goods_name= models.CharField(max_length=200)
    image = models.ImageField(upload_to='')
    feeling_of_use = models.TextField(max_length=1000)
    def __str__(self):
        return self.goods_name
    class Meta:
        verbose_name = "商品テーブル"
        verbose_name_plural = "商品テーブル"