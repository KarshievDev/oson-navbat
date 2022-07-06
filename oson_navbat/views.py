from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#pages

def index_uz_html(request):
    return render(request, 'oson_navbat/index_uz.html')

def about_us_uz_html(request):
    return render(request, 'oson_navbat/about-us_uz.html')

def services_uz_html(request):
    return render(request, 'oson_navbat/services_uz.html')

def blog_uz_html(request):
    return render(request, 'oson_navbat/blog_uz.html')

def contact_uz_html(request):
    return render(request, 'oson_navbat/contact_uz.html')

def sign_in_uz_html(request):
    return render(request, 'oson_navbat/sign-in_uz.html')

def sign_up_uz_html(request):
    return render(request, 'oson_navbat/sign-up_uz.html')

def single_blog_uz_html(request):
    return render(request, 'oson_navbat/single-blog_uz.html')

## language

def ru(request):
    return render(request, 'oson_navbat/index_ru.html')
def en(request):
    return render(request, 'oson_navbat/index_en.html')
def uz(request):
    return render(request, 'oson_navbat/index_uz.html')


#ru section

def index_ru_html(request):
    return render(request, 'oson_navbat/index_ru.html')

def about_us_ru_html(request):
    return render(request, 'oson_navbat/about-us_ru.html')

def services_ru_html(request):
    return render(request, 'oson_navbat/services_ru.html')

def blog_ru_html(request):
    return render(request, 'oson_navbat/blog_ru.html')

def contact_ru_html(request):
    return render(request, 'oson_navbat/contact_ru.html')

def sign_in_ru_html(request):
    return render(request, 'oson_navbat/sign-in_ru.html')

def sign_up_ru_html(request):
    return render(request, 'oson_navbat/sign-up_ru.html')

def single_blog_ru_html(request):
    return render(request, 'oson_navbat/single-blog_ru.html')

#en section

def index_en_html(request):
    return render(request, 'oson_navbat/index_en.html')

def about_us_en_html(request):
    return render(request, 'oson_navbat/about-us_en.html')

def services_en_html(request):
    return render(request, 'oson_navbat/services_en.html')

def blog_en_html(request):
    return render(request, 'oson_navbat/blog_en.html')

def contact_en_html(request):
    return render(request, 'oson_navbat/contact_en.html')

def sign_in_en_html(request):
    return render(request, 'oson_navbat/sign-in_en.html')

def sign_up_en_html(request):
    return render(request, 'oson_navbat/sign-up_en.html')

def single_blog_en_html(request):
    return render(request, 'oson_navbat/single-blog_en.html')

