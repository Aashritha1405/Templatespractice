from django.urls import path 
from .views import * 

urlpatterns=[
    path('signup/',signup,name='signup'),
    path('login/',login_view,name="login"),
    path('get_user/',get_user,name="getuser"),
    path('logout/',logoutF,name="logout"),
    path('create/',create,name="create"),
    path('todo/',todo,name="todo"),
    path('update/<id>',update,name="update"),
    path('delete/<id>',delete,name="delete")
]