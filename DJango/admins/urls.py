from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.admin_dashboard),
    path('show-user', views.get_user),
    path('update-user-to-admin/<int:user_id>', views.update_user_to_admin),
    path('admin_register_user', views.admin_register_user),
]