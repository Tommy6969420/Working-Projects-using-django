from django.urls import path
from. import views
urlpatterns=[
    path("",views.login,name="welcome"),
    path("signup/",views.index, name="signup"),
    path("login/",views.login, name="login"),
    path('home/@<username>',views.home, name='home'),
    path('@<username>',views.profile,name="profile"),
    path('friends/',views.friends,name="friends"),
    path("settings/",views.SettingView.as_view(),name="settings"),
    
]