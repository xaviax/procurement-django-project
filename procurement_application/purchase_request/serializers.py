from rest_framework import serializers
from .models import *



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=["id", "name"]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=["id","name","parent"]


class ProductSerializer(serializers.ModelSerializer):
    model=Products
    fields=["id","name","category"]



class PurchaseRequestSerializer(serializers.ModelSerializer):

        requested_by = serializers.ReadOnlyField(source="requested_by.username")
        department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
        category=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
        sub_category=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
        product=serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())


        class Meta:
            model=PurchaseRequest
            fields='__all__'


        






