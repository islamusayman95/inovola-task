from django.core.exceptions import FieldError
from django.db import models


class CoffeeMachine(models.Model):
    COFFEE_MACHINE_LARGE = 'CM1'
    COFFEE_MACHINE_SMALL = 'CM0'
    ESPRESSO_MACHINE = 'EM0'

    BASE_MODEL = 1
    PREMIUM_MODEL = 2
    DELUXE_MODEL = 3

    PRODUCT_TYPE_CHOICES = [
        (COFFEE_MACHINE_LARGE, 'large machine'),
        (COFFEE_MACHINE_SMALL, 'small machine'),
        (ESPRESSO_MACHINE, 'espresso machine'),
    ]

    MODEL_CHOICES = [
        (BASE_MODEL, 'base model'),
        (PREMIUM_MODEL, 'premium model'),
        (DELUXE_MODEL, 'deluxe model')
    ]

    product_type = models.CharField(max_length=3, choices=PRODUCT_TYPE_CHOICES)
    water_line_compatible = models.BooleanField()
    model = models.PositiveSmallIntegerField(choices=MODEL_CHOICES)

    @property
    def sku(self):
        return f'{self.product_type}{1 if self.water_line_compatible else 0}{self.model}'

    @sku.setter
    def sku(self, value: str):
        value = value.strip()
        try:
            product_type = value[0:3]
            water_line_compatible = value[3] == '1'
            model = value[4]

            self.product_type = product_type
            self.water_line_compatible = water_line_compatible
            self.model = model

        except (ValueError, IndexError, FieldError):
            pass

    def __str__(self):
        return f'<CoffeeMachine {self.pk} - ' \
               f'product_type: {self.product_type}, ' \
               f'water_line_compatible: {self.water_line_compatible}, ' \
               f'model: {self.model}>'


class CoffeePod(models.Model):
    COFFEE_POD_LARGE = 'CP1'
    COFFEE_POD_SMALL = 'CP0'
    ESPRESSO_POD = 'EM0'

    COFFEE_FLAVOR_VANILLA = 0
    COFFEE_FLAVOR_CARAMEL = 1
    COFFEE_FLAVOR_PSL = 2
    COFFEE_FLAVOR_MOCHA = 3
    COFFEE_FLAVOR_HAZELNUT = 4

    ONE_DOZEN = 1
    THREE_DOZEN = 3
    FIVE_DOZEN = 5
    SEVEN_DOZEN = 7

    PRODUCT_TYPE_CHOICES = [
        (COFFEE_POD_LARGE, 'large coffee pod'),
        (COFFEE_POD_SMALL, 'small coffee pod'),
        (ESPRESSO_POD, 'espresso pod'),
    ]

    COFFEE_FLAVOR_CHOICES = [
        (COFFEE_FLAVOR_VANILLA, 'vanilla'),
        (COFFEE_FLAVOR_CARAMEL, 'caramel'),
        (COFFEE_FLAVOR_MOCHA, 'mocha'),
        (COFFEE_FLAVOR_PSL, 'psl'),
        (COFFEE_FLAVOR_HAZELNUT, 'hazelnut'),
    ]

    PACK_SIZE_CHOICES = [
        (ONE_DOZEN, '1 dozen'),
        (THREE_DOZEN, '3 dozen'),
        (FIVE_DOZEN, '5 dozen'),
        (SEVEN_DOZEN, '7 dozen'),
    ]

    product_type = models.CharField(max_length=3, choices=PRODUCT_TYPE_CHOICES)
    coffee_flavor = models.PositiveSmallIntegerField(choices=COFFEE_FLAVOR_CHOICES)
    pack_size = models.PositiveSmallIntegerField(choices=PACK_SIZE_CHOICES)

    @property
    def sku(self):
        return f'{self.product_type}{self.coffee_flavor}{self.pack_size}'

    @sku.setter
    def sku(self, value: str):
        value = value.strip()
        try:
            product_type = value[0:3]
            coffee_flavor = value[3]
            pack_size = value[4]

            self.product_type = product_type
            self.coffee_flavor = coffee_flavor
            self.pack_size = pack_size

        except (ValueError, IndexError, FieldError):
            pass

    def __str__(self):
        return f'<CoffeePod {self.pk} - ' \
               f'product_type: {self.product_type}, ' \
               f'coffee_flavor: {self.coffee_flavor}, ' \
               f'pack_size: {self.pack_size}>'
