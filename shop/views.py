from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):      #This function lists all of the products available.  The category_slug attribute is if a user selects a category
    category=None
    categories = Category.objects.all()     #Querying all categories from database
    products = Product.objects.all()  #Querying all the products from the database
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)      #If a category is selected, then it will be filtered by category
        products = Product.objects.filter(category=category)

    context = {                     #Making a data dictionary to pass to the list.html template
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):      #This function is for the display of a single product when it is selected
    product = get_object_or_404(Product, id=id, slug=slug)  #Using a query by id and slug to get the product
    cart_product_form = CartAddProductForm()
    context = {                     #Making a data dictionary to be able to pass to the detail.html page
        'product': product,
        'cart_product_form': cart_product_form          #This is now passing the cart object form so that the items can be added to the cart
    }
    return render(request, 'shop/product/detail.html', context)