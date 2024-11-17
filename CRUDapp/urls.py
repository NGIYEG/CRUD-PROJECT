from django.urls import path
from. import views

urlpatterns = [
 path('',views.create_item,name='item_list'),
 path('create',views.create_item,name='create_item'),
 path('<int:pk>',views.update_item,name='update_item'),
 path('<int:pk>/delete',views.delete_item,name='delete_item'),
]
