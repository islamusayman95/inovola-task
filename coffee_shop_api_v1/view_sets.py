from rest_framework import viewsets

from .models import CoffeeMachine, CoffeePod

from .serializers import CoffeeMachineSerializer, CoffeePodSerializer


class CoffeeMachineViewSet(viewsets.ModelViewSet):
    queryset = CoffeeMachine.objects.all()
    serializer_class = CoffeeMachineSerializer

    def get_queryset(self):
        query_set = self.queryset
        data_format = self.request.query_params.get('format')

        if self.request.query_params and not data_format:
            product_type = self.request.query_params.get('product_type')
            water_line_compatible = self.request.query_params.get('water_line_compatible')
            model = self.request.query_params.get('model')
            sku = self.request.query_params.get('sku')

            if sku:
                container = CoffeeMachine()
                container.sku = sku

                query_set = query_set.filter(product_type=container.product_type,
                                             water_line_compatible=container.water_line_compatible,
                                             model=container.model)

            elif product_type or model or water_line_compatible is not None:
                if product_type:
                    query_set = query_set.filter(product_type=product_type)

                if water_line_compatible:
                    query_set = query_set.filter(water_line_compatible=water_line_compatible)

                if model:
                    query_set = query_set.filter(model=model)

            else:
                query_set = query_set.none()

        return query_set


class CoffeePodViewSet(viewsets.ModelViewSet):
    queryset = CoffeePod.objects.all()
    serializer_class = CoffeePodSerializer

    def get_queryset(self):
        query_set = self.queryset
        data_format = self.request.query_params.get('format')

        if self.request.query_params and not data_format:
            product_type = self.request.query_params.get('product_type')
            coffee_flavor = self.request.query_params.get('coffee_flavor')
            pack_size = self.request.query_params.get('pack_size')
            sku = self.request.query_params.get('sku')

            if sku:
                container = CoffeePod()
                container.sku = sku

                query_set = query_set.filter(product_type=container.product_type,
                                             coffee_flavor=container.coffee_flavor,
                                             pack_size=container.pack_size)

            elif product_type or coffee_flavor or pack_size:
                if product_type:
                    query_set = query_set.filter(product_type=product_type)

                if coffee_flavor:
                    query_set = query_set.filter(coffee_flavor=coffee_flavor)

                if pack_size:
                    query_set = query_set.filter(pack_size=pack_size)
            else:
                query_set = query_set.none()

        return query_set
