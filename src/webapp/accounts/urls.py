from django.conf.urls import url
from accounts import views
app_name = 'accounts'

urlpatterns = [
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^user_logout/$', views.user_logout,name='user_logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/edit_user_profile/$', views.edit_user_profile, name='edit_user_profile'),
    url(r'^profile/password/$', views.change_password, name='change_password'),
    url(r'^login_error/$',views.login_error,name='login_error'),
    url(r'^password_change_error/$',views.password_change_error,name='password_change_error'),
    url(r'^account_inactive_error/$',views.account_inactive_error,name='account_inactive_error'),
    ]
