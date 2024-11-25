from django.urls import path
from django.views.generic import RedirectView
from .Login import user_list, register_user, login_user, home_view, index, delete_user, confirm_delete
# ,verify_user

urlpatterns = [
    path('', RedirectView.as_view(url='index/', permanent=False)),
    path('users/', user_list, name='user_list'),
    path('users/<str:username>/<str:user_id>/', user_list, name='user_list'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('home/<str:username>/<str:user_id>/', home_view, name='home'),
    # path('home/<str:username>/<str:user_id>/', home_view, name='home'),
    path('index/', index, name='index'),
    path('delete_user/<str:user_id>/', delete_user, name='delete_user'),  
    path('confirm_delete/<str:user_id>/', confirm_delete, name='confirm_delete'),
    # path('verify_user/<str:user_id>/', verify_user, name='verify_user'),  
]
