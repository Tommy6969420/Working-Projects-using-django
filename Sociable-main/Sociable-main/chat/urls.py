from django.urls import path
from. import views
urlpatterns = [
    path('login/',views.authenticate,name='chatLogin'),
    path("",views.index,name='chat'),
    path('get-api/',views.MessagingView1.as_view(),name="update-message"),
    path('get-api/<int:reciever>/<int:sender>',views.get_message,name="get-message"),
    path('post-api/',views.post_message,name="post-message"),
    path('get-user/<int:id>',views.get_user),
    path('msg-api/<int:reciever>/<int:sender>',views.continous_chat,name="msg-api"),
    path("add-connects/",views.ConnectView.as_view(),name="add-connects"),
]
