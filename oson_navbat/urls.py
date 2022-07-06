from django.urls import path
from oson_navbat import views


urlpatterns = [
    #uz
    path('', views.index_uz_html, name=""),
    path('about-us_uz/', views.about_us_uz_html, name='about-us_uz/'),
    path('services_uz/', views.services_uz_html, name='services_uz/'),
    path('blog_uz/', views.blog_uz_html, name='blog_uz/'),
    path('contact_uz/', views.contact_uz_html, name='contact_uz/'),
    path('sign-in_uz/', views.sign_in_uz_html, name='sign-in_uz/'),
    path('sign-up_uz/', views.sign_up_uz_html, name='sign-up_uz/'),
    path('single-blog_uz/', views.single_blog_uz_html, name='single-blog_uz/'),

    #ru
    path('about-us_ru/', views.about_us_ru_html, name='about-us_ru/'),
    path('services_ru/', views.services_ru_html, name='services_ru/'),
    path('blog_ru/', views.blog_ru_html, name='blog_ru/'),
    path('contact_ru/', views.contact_ru_html, name='contact_ru/'),
    path('sign-in_ru/', views.sign_in_ru_html, name='sign-in_ru/'),
    path('sign-up_ru/', views.sign_up_ru_html, name='sign-up_ru/'),
    path('single-blog_ru/', views.single_blog_ru_html, name='single-blog_ru/'),

    #en
    path('about-us_en/', views.about_us_en_html, name='about-us_en/'),
    path('services_en/', views.services_en_html, name='services_en/'),
    path('blog_en/', views.blog_en_html, name='blog_en/'),
    path('contact_en/', views.contact_en_html, name='contact_en/'),
    path('sign-in_en/', views.sign_in_en_html, name='sign-in_en/'),
    path('sign-up_en/', views.sign_up_en_html, name='sign-up_en/'),
    path('single-blog_en/', views.single_blog_en_html, name='single-blog_en/'),

    #language
    path('ru/', views.ru, name='ru/'),
    path('uz/', views.uz, name='uz/'),
    path('en/', views.en, name='en/'),
]

