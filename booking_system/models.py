from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator 

STATUS = ((0, "Draft"), (1, "Published"))
 
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
 
class Booking_details(models.Model):
    date = models.DateTimeField
    slug = models.SlugField(max_length=200, unique=True)
    first_name = models.CharField(max_length=40, unique=True)
    last_name = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=254)
    party_size = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    tables = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    additional_information = models.CharField(max_length=200, unique=True)
    allergies = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.last_name} party of: {self.party_size}'
        'book_now.html'

