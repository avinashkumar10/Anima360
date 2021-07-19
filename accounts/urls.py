from django.views.generic import TemplateView

from .views import RegisterAPI, LoginAPI, ChangePasswordView
from knox import views as knox_views
from django.urls import path, include

from accounts import views
from sahash import settings

app_name="accounts"
urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/user-complain-screen-1/', views.image_upload_view),
    path('api/user-complain-screen-3/', views.save_feedback, name="save_feedback"),
    path('api/user-complain-screen-4/', views.message_view, name="Take_action"),
    path('api/register-shelter-screen-2/', views.shelter, name="shelter"),
    path('api/shelter-facilities-screen-3/', views.facilities, name="facilities"),
    path('api/shelter-facilities-screen-4/', views.billing, name="billing"),

]
