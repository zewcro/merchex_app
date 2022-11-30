from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
        path('admin/', admin.site.urls),
        # bands urls 
        path('bands/', views.band_list, name='band-list'),
        path('bands/<int:id>/', views.band_detail, name='band-detail'),
        path('bands/add/', views.band_create, name='band-create'),
        # other urls 
        path('contact-us/', views.contact, name='contact'),
        path('email-sent', views.email_sent, name='email-sent'),


]
