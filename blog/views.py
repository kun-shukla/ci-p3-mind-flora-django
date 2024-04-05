from django.shortcuts import render
# from django.views import generic
from .models import Post, UserRecommendedDestination
from .forms import ShareDiscoveryForm


# Create your views here.

def post_list(request):
    post_list = Post.objects.filter(status=1)
    if request.method == "POST":
        share_form = ShareDiscoveryForm(data=request.POST)
        if share_form.is_valid():
            share_form.save()
            
    share_form = ShareDiscoveryForm()

    return render(
        request,
        "blog/index.html",
        {
            "post_list": post_list,
            "share_form": share_form,
        },
    )


