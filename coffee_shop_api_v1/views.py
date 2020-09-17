from django.core.exceptions import MultipleObjectsReturned
from django.http import JsonResponse
from django.shortcuts import render

from django.views import View

from .models import CoffeeMachine, CoffeePod


class Index(View):
    def get(self, request):
        context = dict()
        return render(request, 'coffee_shop_api_v1/index.html')


class PopulateData(View):
    def get(self, request):
        sku_list = [
            'CM001',
            'CM002',
            'CM013',
            'CM101',
            'CM112',
            'CM103',
            'EM001',
            'EM002',
            'EM013',
            'CP001',
            'CP003',
            'CP011',
            'CP013',
            'CP021',
            'CP023',
            'CP031',
            'CP033',
            'CP041',
            'CP043',
            'CP101',
            'CP103',
            'CP111',
            'CP113',
            'CP121',
            'CP123',
            'CP131',
            'CP133',
            'CP141',
            'CP143',
            'EP003',
            'EP005',
            'EP007',
            'EP013',
            'EP015',
            'EP017',
        ]

        objects = list()
        for sku in sku_list:
            if sku.__contains__('M'):
                container = CoffeeMachine()
                container.sku = sku

                coffee_machine, new = CoffeeMachine.objects.get_or_create(
                    product_type=container.product_type,
                    water_line_compatible=container.water_line_compatible,
                    model=container.model)
                objects.append(coffee_machine.sku)

            else:
                container = CoffeePod()
                container.sku = sku

                coffee_pod, new = CoffeePod.objects.get_or_create(
                    product_type=container.product_type,
                    coffee_flavor=container.coffee_flavor,
                    pack_size=container.pack_size)
                objects.append(coffee_pod.sku)

        return JsonResponse({
            'Success': True,
            'objects': objects
        })
