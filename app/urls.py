from django.urls import path
from . import views
from django.contrib.auth import views as authViews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('exit', views.logout, name='exit'),
    path('add_order_items/<str:item_type>/<str:item_uid>/', views.AddOrderItemView.as_view(), name='add_order_items'),
    path('remove_items/<str:item_type>/<str:uid>/', views.RemoveOrderItemsView.as_view(), name='remove_order_items'),
    path('success', views.success, name='success'),
    path('order/', views.order, name='order'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
