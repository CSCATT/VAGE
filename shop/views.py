from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .settings.base import *

base_dict = {'phone_number': PHONE_NUMBER,
              'mail': EMAIL,
              'address': ADDRESS,
              'rsm': RIGHT_SIDE_MESSAGE,
              'blsm': BOTTOM_LEFT_SIDE_MESSAGE,
              'vf': VEGEFOODS}

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'shop/index.html', base_dict)

class ShopView(View):
    def get(self, request):

        products = [{'name':       'Bell Pepper',
                     'image':      'shop/images/product-1.jpg',
                     'price':      '$120.00',
                     'discount':   '30%',
                     'price_sale': '$80.00'},
                    {'name':       'Strawberry',
                     'image':      'shop/images/product-2.jpg',
                     'price':      '$120.00'},
                    {'name':       'Green Beans',
                     'image':      'shop/images/product-3.jpg',
                     'price':      '$120.00'},
                    {'name':       'Purple Cabbage',
                     'image':      'shop/images/product-4.jpg',
                     'price':      '$120.00'},
                    {'name':       'Tomatoe',
                     'image':      'shop/images/product-5.jpg',
                     'price':      '$120.00',
                     'discount':   '30%',
                     'price_sale': '$80.00'},
                    {'name':       'Brocolli',
                     'image':      'shop/images/product-6.jpg',
                     'price':      '$120.00'},
                    {'name':       'Carrots',
                     'image':      'shop/images/product-7.jpg',
                     'price':      '$120.00'},
                    {'name':       'Fruit Juice',
                     'image':      'shop/images/product-8.jpg',
                     'price':      '$120.00'},
                    {'name':       'Onion',
                     'image':      'shop/images/product-9.jpg',
                     'price':      '$120.00',
                     'discount':   '30%',
                     'price_sale': '$80.00'},
                    {'name':       'Apple',
                     'image':      'shop/images/product-10.jpg',
                     'price':      '$120.00'},
                    {'name':       'Garlic',
                     'image':      'shop/images/product-11.jpg',
                     'price':      '$120.00'},
                    {'name':       'Chilli',
                     'image':      'shop/images/product-12.jpg',
                     'price':      '$120.00'}]

        return render(request, 'shop/shop.html', {'products': products, 'phone_number': PHONE_NUMBER,
              'mail': EMAIL,
              'address': ADDRESS,
              'rsm': RIGHT_SIDE_MESSAGE,
              'blsm': BOTTOM_LEFT_SIDE_MESSAGE,
              'vf': VEGEFOODS})


class AboutView(View):
    def get(self, request):
        return render(request, 'shop/about.html', base_dict)

wishlist_count = 0
class WishlistView(View):
    def get(self, request):
        return render(request, 'shop/wishlist.html', base_dict)

    def post(self, request):
        global wishlist_count
        if request.is_ajax():
            message = f'WishlistView: {wishlist_count}'
            wishlist_count += 1
            print(message)
        else:
            message = 'Not AJAX request'

        return HttpResponse(message)

class ContactView(View):
    def get(self, request):
        return render(request, 'shop/contact.html', base_dict)

class BlogView(View):
    def get(self, request):
        blogs = [{'author': 'Bell Pepper',
                     'date': 'shop/images/product-1.jpg',
                     'price': '$120.00',
                     'discount': '30%',
                     'price_sale': '$80.00'}]

        return render(request, 'shop/blog.html', {'blogs': blogs, 'phone_number': PHONE_NUMBER,
              'mail': EMAIL,
              'address': ADDRESS,
              'rsm': RIGHT_SIDE_MESSAGE,
              'blsm': BOTTOM_LEFT_SIDE_MESSAGE,
              'vf': VEGEFOODS})
