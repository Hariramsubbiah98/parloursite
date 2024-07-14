from django.db import models
import datetime
import os
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

def get_first_two_letters(text):
    if text:
        return text[:2]
    return 'image'

def getfilenames(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{timestamp}{file_extension}"
    return os.path.join('uploads/', new_filename)


def getfilename(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    author_initials = get_first_two_letters(instance.author)
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{author_initials}_{timestamp}{file_extension}"
    return os.path.join('uploads/', new_filename)
    

class Catagory(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getfilenames,blank=True,null=True)
    description = models.TextField(max_length=200,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-Avaliable 1-Suspended")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    

class Product(models.Model):
    category = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getfilenames,blank=True,null=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    short_description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False,help_text="0-Avaliable 1-Suspended")
    trending = models.BooleanField(default=False,help_text="0-Famous 1-Unfamous")
    created_at = models.DateTimeField(auto_now_add=True)
    original_price = models.FloatField(null=True,blank=True)
    selling_price = models.FloatField(null=True,blank=True)
    
    
    def __str__(self):
        return self.name
        
        
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='additional_images')
    image1 = models.ImageField(upload_to=getfilenames, blank=True, null=True)
    image2 = models.ImageField(upload_to=getfilenames, blank=True, null=True)
    image3 = models.ImageField(upload_to=getfilenames, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class CallbackRequest(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False,help_text="Name")
    email = models.EmailField(max_length=50,null=False,blank=False,help_text="Email Address")
    phone_number = models.CharField(max_length=10,null=False,blank=False,help_text="Mobile No")
    created_at = models.DateTimeField(auto_now_add=True)
    Message =  models.CharField(max_length=150,null=False,blank=False,help_text="Customer Message")
    service =  models.CharField(max_length=50,null=False,blank=False,help_text="Customer intrested service")

    def __str__(self):
        return f"Callback request from {self.name}"
        
        
class ReviewAndRating(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], null=False, blank=False)  
    status = models.BooleanField(default=False, help_text="0-Available 1-Suspended")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=getfilename, blank=True, null=True)
    text = models.CharField(max_length=250, null=False, blank=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
   
    
class blogcat(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250, null=False, blank=False)
    description_title1 = models.CharField(max_length=100, null=True, blank=True)
    description1 = models.CharField(max_length=250, null=True, blank=True)
    description_title2 = models.CharField(max_length=100, null=True, blank=True)
    description2 = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to=getfilenames, blank=True, null=True)
    status = models.BooleanField(default=False, help_text="0-Available 1-Suspended")
    author =  models.CharField(max_length=100, null=False, blank=False)
    About_Author =  models.CharField(max_length=200, null=False, blank=False)
    slug = models.CharField(max_length=10, null=False, blank=False)
    
    
    def __str__(self):
        return self.title
        
        
class faq(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    question = models.CharField(max_length=50, null=False, blank=False)
    answers = models.CharField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-Available 1-Suspended")
    
    def __str__(self):
        return self.title