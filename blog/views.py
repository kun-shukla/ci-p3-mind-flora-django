from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ShareDiscoveryForm, CommentForm
from .models import About, AboutSectionNavImage, Post, ShareDiscoveryFormBgVid, Comment


def post_list(request):
    """
    Displays all 'Published' instances of :model:`blog.Post`. Renders the most recent 'About' section information as well as the circular nav images of this section. Also renders the 'Form' section bg video and allows user content submissions via the 'Share a Discovery' form.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    post_list = Post.objects.filter(status=1)
    about_sec_imgs = AboutSectionNavImage.objects.all().order_by('created_on')
    about = About.objects.all().order_by('-updated_on').first()
    share_form_bg_vid = ShareDiscoveryFormBgVid.objects.all()
    if request.method == "POST":
        share_form = ShareDiscoveryForm(data=request.POST)
        if share_form.is_valid():
            share_form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for your contribution! We endeavour to review and respond within 3 working days.")

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
    ``comments``
        All approved comments related to the post
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.

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
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

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


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`
    ``comment``
        A single comment related to the post
    ``comment_form``
        An instance of :form:`blog.CommentForm`.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`
    ``comment``
        A single comment related to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
