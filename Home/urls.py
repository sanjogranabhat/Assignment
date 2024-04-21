from django.urls import path
from . import views

urlpatterns =[
    path('',views.index ,name="index"),
    path('sanjog/',views.admin,name="admin"),
    path('add_vegetable/',views.add_vegetable,name="add_vegetable"),
    path('update_vegetable/<int:id>/',views.update_vegetable,name='update_vegetable'),
    path('delete_vegetable/<int:id>/',views.delete_vegetable,name='delete_vegetable'),
    
    path('add_fruits/',views.add_fruit,name="add_fruit"),
    path('update_fruit/<int:id>/',views.update_fruit,name='update_fruit'),
    path('delete_fruit/<int:id>/',views.delete_fruit,name='delete_fruit')
    
]
