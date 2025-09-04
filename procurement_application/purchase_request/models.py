from django.db import models
from django.conf import settings
# Create your models here.


class Department(models.Model):
    name=models.CharField(max_length=120,unique=True)


class Category(models.Model):
    name=models.CharField(max_length=120)
    parent=models.ForeignKey(
        "self", null=True,blank=True
        ,related_name="subcategories",
        on_delete=models.CASCADE
    )
    
    class Meta:
        unique_together=("name","parent")

    def __str__(self):
        return f"{self.parent.name} -> {self.name}" if self.parent else self.name





class Products(models.Model):
    name=models.CharField(max_length=120)
    category=models.ForeignKey(Category,related_name="products",on_delete=models.PROTECT)


    def __str__(self):
        return self.name




class PurchaseRequest(models.Model):
    STATUS_DRAFT = "DRAFT"
    STATUS_PENDING = "PENDING"
    STATUS_SUBMITTED = "SUBMITTED"
    STATUS_APPROVED = "APPROVED"
    STATUS_REJECTED = "REJECTED"

    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_PENDING, "Pending"),
        (STATUS_SUBMITTED, "Submitted"),
        (STATUS_APPROVED, "Approved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    created_at=models.DateTimeField(auto_now_add=True)

    requested_by = models.ForeignKey(

        settings.AUTH_USER_MODEL,
        related_name="purchase_requests",
        on_delete=models.CASCADE,


    )

    department = models.ForeignKey(Department,related_name="purchase_requests", on_delete=models.PROTECT)

    justification= models.TextField()

    category= models.ForeignKey(Category,related_name="purchase_requests",on_delete=models.SET_NULL, null=True,
                                blank=True)

    sub_category=models.ForeignKey(Category, related_name="purchase_requests_as_subcategory",
                                   on_delete=models.SET_NULL, null=True)

    product = models.ForeignKey(Products,related_name="purchase_request", on_delete=models.SET_NULL, null=True,
                                blank=True)


    status= models.CharField(choices=STATUS_CHOICES,default=STATUS_PENDING)


    class Meta:
        ordering =["-created_at"]







