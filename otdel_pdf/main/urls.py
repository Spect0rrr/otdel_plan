from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('admin-panel/', views.admin_panel, name='adminPanel'),
    path('new-user/', views.new_user, name='newUser'),
    path('delete-user/', views.delete_user, name='deleteUser'),
    path('change-password/', views.change_password, name='changePassword')
]
