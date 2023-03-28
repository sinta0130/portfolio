from django.shortcuts import render

# Create your views here.

from .models import Goods


def index(request):
    goods_list = Goods.objects.all()
    # print(goods_list)
    context = {'goods_list': goods_list}
    # print(context)
    return render(request, 'cola/index.html', context)

def detail(request, goods_id):
    print(goods_id)
    goods = Goods.objects.select_related('category').filter(id=goods_id).values(
        'goods_name',
        'image',
        'feeling_of_use',
        'category__category_name'
    )
    print(goods[0]['category__category_name'])
    context = {'goods':goods}
    return render(request, 'cola/detail.html', context)

