from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from apps.home.models import Banner, Category, Navigation, ShopImage


def index(request):
      # 获取导航菜单数据

    navigations = Navigation.objects.all()

    # 获取分类菜单数据

    categories = Category.objects.all()
    for category in categories:
        category.subs = category.submenu_set.all()
        for sub in category.subs:
            sub.sub2 = sub.submenu2_set.all()
        category.shops=category.shop_set.all().values('shop_id','name','promote_price')
        for shop in category.shops:
            shop.update(img=ShopImage.objects.filter(shop_id=shop.get('shop_id')).first())






    # 轮播图数据
    banners = Banner.objects.all()

    return render(request,'index.html',{'navigations':navigations,'banners':banners,'categories':categories})