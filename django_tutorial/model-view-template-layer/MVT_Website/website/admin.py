from django.contrib import admin

from website.models import Auction, Bid, Chat, Product, UserDetails, Watchlist

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(Chat)
admin.site.register(Watchlist)
admin.site.register(Bid)