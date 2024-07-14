from django.urls import path
from . import views as v1
from django.contrib.auth import views as auth_views

urlpatterns = [  
    path('', v1.home, name='home'),
    path('services',v1.services,name='service'),
    path('services/<str:name>',v1.servicesview,name='servicesview'),
    path('service/<str:cname>/<str:pname>',v1.product_details,name="product_details"),
    path('callback',v1.callback,name='callback'),
    path('review',v1.reviewpage,name='reviews'),
    path('loadmorereviews',v1.loadmore,name='loadmore'),
    path('submitreview',v1.submit,name='submitreview'),
    path('blogs',v1.blog,name='blog'),
    path('blogs/<str:tname>',v1.blogview,name='blogview'),
    path('faqs',v1.faqpage,name='faqpage'),
    path('aboutus',v1.aboutus,name='aboutus'),
    path('test',v1.test,name='test'),
]
