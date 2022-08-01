from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AuctionBids(models.Model):
    id = models.IntegerField()


class AuctionItem(models.Model):
    name = models.CharField(max_length=64)
    basePrice = models.FloatField()
    pictureUrl = models.CharField(max_length=200)
    description = models.CharField(max_length=254)
    createdDate = models.DateField()
    bids = models.ForeignKey(AuctionBids)


class Bid(models.Model):
    value = models.IntegerField()
