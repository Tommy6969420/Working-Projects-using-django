from django.urls import path
from. import views
urlpatterns = [
    path('admission/',views.admission,name='admission')
]
