from django.urls import path

from apps.views import HomePageView, AboutPageView, ShopPageView, ContactPageView, SinglePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('shop/', ShopPageView.as_view(), name='shop'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('single/<slug:slug>', SinglePageView.as_view(), name='shop_single'),
]
