from django.urls import path 
from . import views

urlpatterns=[
    path('',views.homeblog, name ='homeblog'),
    path('about/',views.about, name="about"),
    path('formations/',views.formations, name="formations"),
    path('contact/', views.contact_view, name='contact_view'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path("article/<int:article_id>/", views.blog_details, name="blog_details"),

    path('tarifs/', views.tarifs, name='tarifs'),

   
]
