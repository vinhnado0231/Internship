from django.contrib.auth.models import User
from django.shortcuts import render

from django.utils import timezone
from datetime import datetime
from itertools import chain

from website.forms import *
from website.models import Product, Auction, Watchlist, Bid, Chat, UserDetails

from website.validation import validate_login, validate_registration
from website.transactions import increase_bid, remaining_time

def index(request):
    """
    The main page of the website

    Returns
    -------
    HTTPResponse
        The index page with the current and future auctions.
    """
    auctions = Auction.objects.filter(time_ending__gte=datetime.now()).order_by('time_starting')

    try:
        if request.session['username']:
            user = User.objects.get(username=request.session['username'])

            w = Watchlist.objects.filter(user_id=user)
            watchlist = Auction.objects.none()
            for item in w:
                a = Auction.objects.filter(id=item.auction_id.id)
                watchlist = list(chain(watchlist, a))

            userDetails = UserDetails.objects.get(user_id=user.id)
            return render(request, 'index.html',
                {'auctions': auctions, 'balance': userDetails.balance, 'watchlist': watchlist})
    except KeyError:
        return render(request, 'index.html', {'auctions': auctions})

    return render(request, 'index.html', {'auctions': auctions})

def register_page(request):
    """
    Returns the registration page.

    Returns
    -------
    HTTPResponse
        The registration page.
    """
    print("Vao")
    return render(request, 'register.html')


def register(request):
    """
    Registration POST request.

    Returns
    -------
    Function
        Index page request
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            is_valid = validate_registration(
                form.cleaned_data['username'],
                form.cleaned_data['password1'],
                form.cleaned_data['password2'],
                form.cleaned_data['email']
            )
            if is_valid:
                # Create an User object with the form parameters.
                user = User.objects.create_user(username=form.cleaned_data['username'],
                                                email=form.cleaned_data['email'],
                                                password=form.cleaned_data['password1'])
                user.first_name = form.cleaned_data['firstname']
                user.last_name = form.cleaned_data['lastname']
                user.save()  # Save the object to the database.
                userDetails = UserDetails()
                userDetails.balance = 0.0
                userDetails.cellphone = form.cleaned_data['cellphone']
                userDetails.address = form.cleaned_data['address']
                userDetails.town = form.cleaned_data['town']
                userDetails.post_code = form.cleaned_data['postcode']
                userDetails.country = form.cleaned_data['country']
                userDetails.user_id = user
                userDetails.save()
    return index(request)

def login_page(request):
    """
    Login POST request.
        
    Returns
    -------
    Function
        Index page request    
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            is_valid = validate_login(
                form.cleaned_data['username'], 
                form.cleaned_data['password']
            )
            if is_valid :
                # Creates a session with 'form.username' as key.
                request.session['username'] = form.cleaned_data['username']
    return index(request)

def logout_page(request):
    """
    Deletes the session.
    
    Returns
    -------
    Function
        Index page request
    """
    try:
        del request.session['username']
    except:
        pass # if there is no session pass
    return index(request)