from django.shortcuts import render

# Create your views here.
from apps.home.models import Shop


def detail(request):
    if request.method=="GET":
        shop_id = request.GET.get('id')
        try:
            if shop_id:

               shop= Shop.objects.get(shop_id=shop_id)
               shop.imgs=shop.shopimage_set.all()

            return render(request, 'detail.html', {''})
        except:
            return request(request, "error.html")
    else:
        return request(request, "error.html")

