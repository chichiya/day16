from django.contrib import admin
from django.conf.urls import url,include

from home import views

urlpatterns = [
url('admin/', admin.site.urls),
url('^$',views.index),
url('account/',include('apps.account.urls')),
url('cart/',include('apps.cart.urls')),
url('cate_detail/',include('apps.cate_detail.urls')),
url('home/',include('apps.home.urls')),
url('order/',include('apps.order.urls')),
url('pay/',include('apps.pay.urls')),
url('shop_detail/',include('apps.shop_detail.urls')),
url('search/',include('apps.search.urls')),

]
