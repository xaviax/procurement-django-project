from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()

router.register("departments",views.DepartmentViewSet)
router.register("categories",views.CategoryViewSet)
router.register("products",views.ProductViewSet)
router.register("purchase-requests",views.PurchaseRequestViewSet)

urlpatterns=router.urls

