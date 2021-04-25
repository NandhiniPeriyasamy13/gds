from django.shortcuts import render, HttpResponseRedirect
from .models import *
from ecommerce.models import Product
from django.contrib.auth.decorators import login_required
from ecommerce.views import *
from carts.views import *
from django.urls import reverse
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404
from django.contrib.sessions.models import Session
import time
from django.contrib.auth.models import User
from orders.views import *
from carts.views import *
from accounts.models import *
from accounts.views import *

@login_required
def profile(request):
    request.session.set_expiry(120000)
    user = request.user
    try:
        addressDefault = UserAddress.objects.get(user=request.user)
        context = {'address': addressDefault}
    except:
        addressDefault = None
        context = {}
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()


        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        phone_number = request.POST['phone_number']

        if addressDefault:
            addressDefault.address = address
            addressDefault.city = city
            addressDefault.state = state
            addressDefault.zipcode = zipcode
            addressDefault.phone_number = phone_number
            addressDefault.save()
            messages.success(request, 'Saved successfully')
        else:
            new_address = UserAddress.objects.create(user=request.user, address=address, city=city, state=state,
                                                     zipcode=zipcode, phone_number=phone_number)
            new_address.save()
    return render(request, 'accounts/profile1.html', context)
