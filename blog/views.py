from django.shortcuts import render, get_object_or_404
# from django.views import generic
from .models import Post, About, AboutSectionNavImage, UserRecommendedDestination, ShareDiscoveryFormBgVid
from .forms import ShareDiscoveryForm, CommentForm


# Create your views here.

def post_list(request):
    post_list = Post.objects.filter(status=1)
    about_sec_imgs = AboutSectionNavImage.objects.all().order_by('created_on')
    about = About.objects.all().order_by('-updated_on').first()
    share_form_bg_vid = ShareDiscoveryFormBgVid.objects.all()
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
            "share_form_bg_vid": share_form_bg_vid, 
            "share_form": share_form,
        },
    )

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
         },
    )





