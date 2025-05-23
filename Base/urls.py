from django.urls import path , include
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
    path('app/fera',views.fera, name = 'fera'),

    path('ebook/optimisationia',views.optimisation, name = 'optimisation'),
    path('ebook/bigdata',views.bigdata, name = 'bigdata'),
    path('ebook/nutritionia',views.nutrition, name = 'nutrition'),
    
    path('robots.txt', views.robot, name='robot'),

    path('sitemap.xml', views.sitemap_view, name='sitemap'),

    path('blog/', include('blog.urls')),  # Inclusion des URLs du blog


]
