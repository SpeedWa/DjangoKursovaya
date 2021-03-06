"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(_(r'^cart/'), include(('cart.urls', 'cart'), namespace='cart')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(_(r'orders/'), include(('orders.urls', 'order'), namespace='orders')),
    url(r'^', include(('shop.urls', 'shop'), namespace='shop')),
    url(_(r'^coupons/'), include(('coupons.urls', 'coupons'), namespace='coupons')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
