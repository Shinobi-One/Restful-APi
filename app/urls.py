from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('app',views.All_In_One,basename='app')
router.register('collection' ,views.Collection_Set)
router.register('carts' ,views.CartSet)
router.register('customer',views.CustomerViewSets)
router.register('orders',views.OrderSet,basename='order')

nested_router=routers.NestedDefaultRouter(router , 'app',lookup='app')
nested_router.register('review',views.ReviewSet ,basename="apps_reviews")

cart_router = routers.NestedDefaultRouter(router , 'carts',lookup='cart')
cart_router.register('items',views.CartItemSet,basename='cart_items')


urlpatterns = router.urls + nested_router.urls + cart_router.urls
    # path("app",views.MainList.as_view(),name="Home-page"),
    # path('app/<pk>', views.DETAIL.as_view(), name="id-page"),

