from django.db import models


class Price(models.Model):
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=19, decimal_places=10)
    currency = models.CharField(max_length=10, default='usd')

    class Meta:
        unique_together = ('date', 'currency')

    def __str__(self):
        return f"Precio de Bitcoin al {self.date}"


class MarketData(models.Model):
    date = models.DateTimeField()
    total_volume = models.BigIntegerField()
    market_cap = models.DecimalField(max_digits=19, decimal_places=4)
    market_cap_rank = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10, default='usd')

    class Meta:
        unique_together = ('date', 'currency')

    def __str__(self):
        return f"Datos de Mercado de Bitcoin al {self.date}"
