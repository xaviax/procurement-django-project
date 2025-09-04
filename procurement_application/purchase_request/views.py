from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, action
# Create your views here.

from .models import *
from .serializers import *
from .permissions import *


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):

    queryset=Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]



class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes=[IsAuthenticated]


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[IsAuthenticated]



class PurchaseRequestViewSet(viewsets.ModelViewSet):

    queryset=PurchaseRequest.objects.all()
    serializer_class = PurchaseRequestSerializer
    permission_classes=[IsAuthenticated]


    def get_queryset(self):
        #users can only see their own requests
        #this will work as the users are those in the department coordinator group
        return PurchaseRequest.objects.filter(requested_by=self.request.user)


    def perform_create(self,serializer):
        print("request.user is: ", self.request.user)
        print("request.auth is: ", self.request.auth)

        serializer.save(requested_by=self.request.user)


    def get_permissions(self):

        if self.action== "create":
            return[IsAuthenticated(), IsDepartmentCoordinator()]

        if self.action in ["update","partial_update","destroy","submit"]:
            return [IsAuthenticated(), IsCreator()]

        return [IsAuthenticated()]


    @action(detail=True, methods=["POST"])
    def submit(self,request,pk=None):
        purchase_request = self.get_object()

        purchase_request.save()

        return Response({"message": "Request Submitted"})









