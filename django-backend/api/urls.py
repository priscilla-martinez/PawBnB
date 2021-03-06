from django.urls import path
from .views.users import SignUp, SignIn, SignOut, ChangePassword
from .views.homes import HomesView, HomeView

urlpatterns = [
    # Users 
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),

    # Homes
    path('homes/', HomesView.as_view(), name='homes'),
    path('home/', HomeView.as_view(), name='home'),
    path('home/<int:pk>', HomeView.as_view(), name='home')
]