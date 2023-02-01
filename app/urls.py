from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter,DefaultRouter
from rest_framework_nested import routers


router = DefaultRouter()
router.register('app',views.All_In_One)
router.register('collection' ,views.Collection_Set)

nested_router=routers.NestedDefaultRouter(router , 'app',lookup='app_pk')
nested_router.register('review',views.ReviewSet ,basename="apps_reviews")

urlpatterns = router.urls + nested_router.urls
    # path("app",views.MainList.as_view(),name="Home-page"),
    # path('app/<pk>', views.DETAIL.as_view(), name="id-page"),
    

