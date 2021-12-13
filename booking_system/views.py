from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Booking_details
from django.http import HttpResponse


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

class UserDetails(View):
    def get(self, request, *args, **kwargs):
        queryset = Booking_details.objects.all()
        booking_details = get_object_or_404(queryset)
        return render(
            request,
            "booking_form.html",
            {
                "booking_details": booking_details,
            },
        )


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
            },
        )


class BookNow(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "book_now.html"
    paginate_by = 6