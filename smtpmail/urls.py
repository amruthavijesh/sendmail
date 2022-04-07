from django.urls import path
from . import views
app_name='smtpmail'
urlpatterns=[
    path('',views.index,name='index'),
    path('sendmail',views.sendmail,name='sendmail'),
    path('contactus',views.contactus,name='contactus'),
]