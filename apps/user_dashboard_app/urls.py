from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/admin/', views.reg_admin),
    path('register/admin/process/', views.reg_admin_process),
    path('signin/', views.signin),
    path('signin/process/', views.signin_user_process),
    path('signin/admin/', views.signin_admin),
    path('signin/admin/process/', views.signin_admin_process),
    path('register/', views.register),
    path('register/process/', views.register_process),
    path('dashboard/admin/', views.dashboard_admin),
    path('dashboard/', views.dashboard),
    path('dashboard/admin/remove/<int:id>', views.remove),
    path('users/new/', views.new_user),
    path('users/new/process/', views.new_user_process),
    path('user/<int:id>/', views.user),
    path('user/<int:id>/postmessage/', views.post_message),
    path('user/<int:user_id>/deletemessage/<int:message_id>/', views.delete_message),
    path('user/<int:id>/postcomment/', views.post_comment),
    path('user/<int:user_id>/deletecomment/<int:comment_id>/', views.delete_comment),
    path('users/edit/<int:id>/', views.edit_user),
    path('users/edit/<int:id>/info_process/', views.edit_user_process),
    path('users/edit/<int:id>/password_process/', views.edit_password_process),
    path('users/edit/<int:id>/description_process/', views.description_process),
    path('signout/', views.signout),
]
