from django.urls import path 
from . import views
from django.views.generic import TemplateView

urlpatterns=[
    path('',views.home, name ='home'),
    # path('',views.contact, name="contact"),
    # path('contact/', views.contact, name='contact'),
    path('success/', views.success_view, name='success'),



    path('services/consultations_agtech',views.consultations, name = 'consultations'),
    path('services/developpement_logiciel',views.developpement, name = 'developpement'),
    path('services/marketing_digital',views.marketing, name = 'marketing'),
    path('services/business_intelligent',views.business, name = 'business'),
    path('services/transformation_digital',views.transformation, name = 'transformation'),
    path('app/bangri',views.bangri, name = 'bangri'),
    path('app/bangpig',views.bangpig, name = 'bangpig'),
    path('app/zbang',views.zbang, name = 'zbang'),
    path('app/bangquiz',views.bangquiz, name = 'bangquiz'),

    path('ebook/optimisationia',views.optimisation, name = 'optimisation'),
    path('ebook/bigdata',views.bigdata, name = 'bigdata'),
    path('ebook/nutritionia',views.nutrition, name = 'nutrition'),
    
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),

    path('sitemap.xml', views.sitemap_view, name='sitemap'),


]
