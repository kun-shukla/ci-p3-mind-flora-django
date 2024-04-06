from django.shortcuts import render
# from django.views import generic
from .models import Post, About, AboutSectionNavImage, UserRecommendedDestination
from .forms import ShareDiscoveryForm


# Create your views here.

def post_list(request):
    post_list = Post.objects.filter(status=1).order_by("created_on")
    about_sec_imgs = AboutSectionNavImage.objects.all().order_by('created_on')
    about = About.objects.all().order_by('-updated_on').first()
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
            "about": about,
            "about_sec_imgs": about_sec_imgs,
            "share_form": share_form,
        },
    )





