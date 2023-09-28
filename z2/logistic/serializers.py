from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=4, allow_null=False)
    description = serializers.CharField(allow_blank=False)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description']

    def validate(self, attrs):
        if attrs.get('title') and ';' in attrs['title']:
            raise ValidationError('Error data contains prohibited symbol ;')
        return attrs

    def create(self, validated_data):
        if Product.objects.filter(title=validated_data['title']):
            raise ValidationError('Error product already exists! Product name should be unique.')
        return super().create(validated_data)


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['id', 'quantity', 'price', 'product']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        fields = ['id', 'address', 'products', 'positions']
        model = Stock

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position in positions:
            StockProduct(stock=stock,
                         product=position['product'],
                         quantity=position['quantity'],
                         price=position['price']).save()
        return stock

    def update(self, instance, validated_data):
        if validated_data.get('positions'):
            positions = validated_data.pop('positions')
            for position in positions:
                prod = StockProduct.objects.filter(product=position['product'], stock=instance)
                if not prod:
                    StockProduct(stock=instance,
                                 product=position['product'],
                                 quantity=position['quantity'],
                                 price=position['price']).save()
                else:
                    StockProduct.objects.filter(
                        product_id=position['product'],
                        stock_id=instance.id).update(quantity=position['quantity'], price=position['price'])
        stock = super().update(instance, validated_data)
        return stock
