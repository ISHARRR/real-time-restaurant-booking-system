from django.urls import path, re_path
from . import views
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)

urlpatterns = [
    #  account/
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/password/', views.change_password, name='profile_password'),
    path('change-password', views.change_password, name='change_password'),
    path('reset-password', PasswordResetView.as_view(template_name='accounts/reset_password.html'),
         name='reset_password'),
    path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path('reset-password/confirm(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)',
            PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('home-tables', views.update_tables, name='update_tables'),
    path('reservation', views.view_reservation, name='view_reservation'),
    path('make-reservation', views.make_reservation, name='make_reservation'),
    path('delete-reservation', views.delete_reservation, name='delete_reservation'),
]
