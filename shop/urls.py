from django.shortcuts import redirect
from django.urls import path
from .views import *


urlpatterns = [
	path('', IndexView.as_view(), name='index'),# если не прописываем путь то видим основную страницу. --> VAGE.urls --> shop.views.
	path('shop/', ShopView.as_view(), name='shop'),
	path('about/', AboutView.as_view(), name='about'),

	path('wishlist/', WishlistView.as_view(), name='wishlist'),
	path('wishlist/pic/', lambda request: redirect("https://picsum.photos/100"), name='wishlist-pic'),

	path('contact/', ContactView.as_view(), name='contact'),
	path('blog/', BlogView.as_view(), name='blog')
	]