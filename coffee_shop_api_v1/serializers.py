from rest_framework import serializers
from .models import CoffeeMachine, CoffeePod


class CoffeeMachineSerializer(serializers.HyperlinkedModelSerializer):
    # sku = serializers.SerializerMethodField()
    # product_type = serializers.SerializerMethodField()
    # model = serializers.SerializerMethodField()

    class Meta:
        model = CoffeeMachine
        fields = ['pk', 'product_type', 'water_line_compatible', 'model', 'sku']

    # def get_sku(self, coffee_machine: CoffeeMachine):
    #     return coffee_machine.sku
    #
    # def get_product_type(self, coffee_machine: CoffeeMachine):
    #     return coffee_machine.get_product_type_display()
    #
    # def get_model(self, coffee_machine: CoffeeMachine):
    #     return coffee_machine.get_model_display()


class CoffeePodSerializer(serializers.HyperlinkedModelSerializer):
    # sku = serializers.SerializerMethodField()
    # product_type = serializers.SerializerMethodField()
    # coffee_flavor = serializers.SerializerMethodField()
    # pack_size = serializers.SerializerMethodField()

    class Meta:
        model = CoffeePod
        fields = ['pk', 'product_type', 'coffee_flavor', 'pack_size', 'sku']

    # def get_sku(self, coffee_pod: CoffeePod):
    #     return coffee_pod.sku
    #
    # def get_coffee_flavor(self, coffee_pod: CoffeePod):
    #     return coffee_pod.get_coffee_flavor_display()
    #
    # def get_product_type(self, coffee_pod: CoffeePod):
    #     return coffee_pod.get_product_type_display()
    #
    # def get_pack_size(self, coffee_pod: CoffeePod):
    #     return coffee_pod.get_pack_size_display()
