from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import *
from django.core.mail import send_mail
from .forms import CallbackRequestForm,ReviewForm
from django.db.models import Avg
from django.http import JsonResponse
from django.template.loader import render_to_string
import logging
logger = logging.getLogger(__name__)

def home(request):
    product = Product.objects.filter(trending=1)
    return render(request, 'parlour/index.html',{"product":product})
    
def services(request):
    catagory = Catagory.objects.filter(status=0)
    return render(request,'parlour/service.html',{"catagory":catagory})
    
    
def servicesview(request, name):
    category = Catagory.objects.filter(name=name, status=0).first()
    if category:
        products = Product.objects.filter(category__name=name)
        return render(request, 'parlour/collection.html', {"products": products, "category": category})
    else:
        messages.warning(request, "No Service available now")
        return redirect('service')

def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,'parlour/productdetails.html',{"products":products})
        else:
            messages.error(request,'No such Product Found')
            return redirect('servicesview')
    else:
        messages.error(request,'No such Category Found')
        return redirect('servicesview')
        
        
def callback(request):
    form = CallbackRequestForm()
    if request.method == 'POST':
        form = CallbackRequestForm(request.POST)
        if form.is_valid():
            callback_request = form.save()
            person_name = form.cleaned_data.get('name')
            mobile_number = form.cleaned_data.get('phone_number')
            subject = 'New Callback Request Submitted'
            message = (f'A new callback request has been submitted by {person_name}.\n'
                       f'Mobile Number: {mobile_number}\n'
                       f'Please check the admin panel for more details.')
            from_email = 'hariramsubbiah98@gmail.com'
            recipient_list = ['hariramsubbiah98@gmail.com']

            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, "Request submitted")
            return redirect('home')
    return render(request, 'parlour/register.html', {"form": form})
    
    

def reviewpage(request):
    form = ReviewForm()
    total_data = ReviewAndRating.objects.filter(status=0).count()
    reviews =  ReviewAndRating.objects.filter(status=0).order_by('-rating')[:6]
    average_rating = ReviewAndRating.objects.filter(status=0).aggregate(Avg('rating'))['rating__avg']
    return render(request, 'parlour/review.html', {
        'reviews': reviews,
        'average_rating': average_rating,
        'total_data': total_data, 
        'form':form
    })


def loadmore(request):
    try:
        limit = int(request.GET.get('limit', 3))
        offset = int(request.GET.get('offset', 0))
        reviews = ReviewAndRating.objects.filter(status=0)[offset:offset+limit]
        html = render_to_string('parlour/ajax.html', {'reviews': reviews})
        return JsonResponse({'data': html})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
        
        
        
def submit(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review_instance = form.save(commit=False)
            review_instance.ip_address = get_client_ip(request) 
            review_instance.created_at = timezone.now()  
            review_instance.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    
    return render(request, 'review_form.html', {'form': form})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        
    return ip
    
    
    

def blog(request):
    blogs = blogcat.objects.filter(status=0)
    return render(request, 'parlour/blog.html', {'blog': blogs})

def blogview(request, tname):
    blogvi = get_object_or_404(blogcat, slug=tname, status=0)
    other_blogs = blogcat.objects.filter(status=0).exclude(slug=tname).order_by('?')[:3]
    return render(request, 'parlour/blogview.html', {'blogvi': blogvi,'other_blogs':other_blogs})
    
    
def faqpage(request):
    faqs = faq.objects.filter(status=0)
    return render(request,'parlour/faq.html',{'faqs':faqs})
    
    
    
def aboutus(request):
    return render(request,'parlour/aboutus.html')
    
    
    
def test(request):
    return render(request,'parlour/test.html')