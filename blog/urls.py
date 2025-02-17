from django.urls import path 
from . import views

urlpatterns=[
    path('Bangri/',views.homeblog, name ='homeblog'),
    path('about/',views.about, name="about"),
    path('formations/',views.formations, name="formations"),
    path('contact/', views.contact_view, name='contact_view'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('Formation-Formulation-de-precision/', views.aliments, name='aliments'),
    path('Formation-Python/', views.python, name='python'),
    path('Formation-Booster-avec-ia/', views.booster, name='booster'),
    path('aliments/Formulation-de-precision/', views.final_aliment, name='final_aliment'),
    path('python/python-avec-chatgpt/', views.final_python, name='final_python'),
    path('inscription/', views.final_aliment, name='inscription'),
    path('python/booster-votre-productivité-avec-ia/', views.final_booster, name='final_booster'),

    path("article/<int:article_id>/", views.blog_details, name="blog_details"),

    # path('tarifs/', views.tarifs, name='tarifs'),


]
