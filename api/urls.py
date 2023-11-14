from django.urls import path, re_path
from .views import IndexView, RegistrationView, AppView, LogoutView, DownloadView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('registration', RegistrationView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('download/<int:pk>/', DownloadView.as_view(), name='download'),
    re_path(r'^app/$', AppView.as_view(), name='app'),

]