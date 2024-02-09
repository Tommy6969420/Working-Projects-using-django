from django.urls import path
from . import views
urlpatterns = [
    path('auth/', views.authenticate, name='auth'),
    path('meeting/', views.meetings, name='meetings'),

]
