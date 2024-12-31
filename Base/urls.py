from django.urls import path 
from . import views

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
    path('services/bangri',views.bangri, name = 'bangri'),
    path('services/bangpig',views.bangpig, name = 'bangpig'),
    path('services/zbang',views.zbang, name = 'zbang'),
    path('services/bangquiz',views.bangquiz, name = 'bangquiz'),

    path('ebook/optimisationia',views.optimisation, name = 'optimisation'),
    path('ebook/bigdata',views.bigdata, name = 'bigdata'),
    path('ebook/nutritionia',views.nutrition, name = 'nutrition'),
    

]
