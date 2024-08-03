from django.urls import path
from . import views
# from .views import SignUpView

urlpatterns = [
    path('', views.index, name= 'index'),
    path('post/<str:pk>', views.post, name='post'),
    path('signup/',views.signup, name="signup"),
]