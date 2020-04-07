from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Imię')
    second_name = models.CharField(max_length=255, verbose_name='Nazwisko')
    postal_code = models.CharField(max_length=6, verbose_name='Kod pocztowy')
    street = models.CharField(max_length=255, verbose_name='Ulica')
    city = models.CharField(max_length=255, verbose_name='Miasto')
    nip = models.PositiveIntegerField(verbose_name='NIP')

    def __str__(self):
        title = str(self.first_name + ' ' + self.second_name)
        return title


class Order(models.Model):
    STATUS_CHOICES = {'a': '10% przyjęto',
                      'b': '30% w trakcie realizacji',
                      'c': '70% wykonano',
                      'd': '100% wysłano/wydano',
                      }

    client = models.ForeignKey('dayoff.Client', on_delete=models.PROTECT, verbose_name='Klient')
    product = models.CharField(max_length=255, verbose_name='Produkt')
    price = models.PositiveIntegerField(verbose_name='Cena netto')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    begin_date = models.DateField()
    finish_date = models.DateField()
