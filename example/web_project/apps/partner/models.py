# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from affiliate.models import AbstractAffiliate


class Affiliate(AbstractAffiliate):
    pass


class AffiliateTransaction(models.Model):
    affiliate = models.ForeignKey(Affiliate)
    product = models.ForeignKey('products.Product')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    bought_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    reward_amount = models.DecimalField(max_digits=5, decimal_places=2)
    reward_percentage = models.BooleanField(default=False)
    reward = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
