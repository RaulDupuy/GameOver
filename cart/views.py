from django.shortcuts import render, redirect
from cart.cart import Cart
from products.models import Products
from GameOver.forms import userOrderForm
from orders.models import Order, OrderItems

# Create your views here.
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/menu-cart.html')

def cart(request):
    return render(request, 'cart/cart.html')

def checkout(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = userOrderForm(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email': request.user.email})
            return render(request, 'cart/checkout.html', {'form':form})
        else:
            cart = Cart(request)
            form = userOrderForm(request.POST)

            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                street = form.cleaned_data['street']
                number = form.cleaned_data['number']
                flat = form.cleaned_data['flat']
                apartment = form.cleaned_data['apartment']
                city = form.cleaned_data['city']
                province = form.cleaned_data['province']
                code = form.cleaned_data['code']
                phone = form.cleaned_data['phone']

                order = Order.objects.create(
                    user=request.user, 
                    first_name = first_name, 
                    last_name = last_name, 
                    email = email, 
                    street = street, 
                    number = 
                    number, 
                    flat = flat, 
                    apartment = apartment, 
                    city = city, 
                    province = province, 
                    code = code, 
                    phone = phone,
                )

                for item in cart:
                    product = item['product']
                    price = product.price
                    quantity = int(item['quantity'])
                    total_price = price * quantity

                    item = OrderItems.objects.create(
                        order=order,
                        product=product,
                        price = price,
                        quantity = quantity,
                        total_price = total_price,
                    )
                
                return redirect('My profile')
            
            else:
                errors = form.errors.items()
                form = userOrderForm()
                context = {'errors': errors, 'form':form}
                return render(request, 'cart/checkout.html', context)
    else:
        return redirect('/login')

def hx_menu_cart(request):
    return render(request, 'cart/menu-cart.html')

def hx_cart_total(request):
    return render(request, 'cart/part/cart-total.html')

def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)
    
    product = Products.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)['quantity']

    item = {
        'product' : {
            'id' : product.id,
            'name' : product.name,
            'image': product.image,
            'price' : product.price,
        },
        'total_price': (quantity * product.price),
        'quantity' : quantity,
    }

    context = {'item':item}
    response = render(request, 'cart/part/cart-item.html', context)
    response['HX-Trigger'] = 'update-menu-cart'

    return response