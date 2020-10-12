from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
# from .forms import  VideoForm, CommentsForm
from .models import User, Video, Comment


def landing_page(request):
    if request.user.is_authenticated:
        return render (request, 'landing_page.html')
    return render (request, 'landing_page.html')


def homepage(request):
    return render(request, "studiopal/homepage.html")

# def add_comment(request, image_pk):
# video = get_object_or_404(Video, pk = video_pk)
#     if request.method == 'GET':
#         form =VideoForm()
#     else:
#         form=CommentsForm(data = request.POST)
#         if form. is_valid():
#             comments = form.save(commit=False)
#             comments.author = request.user
#             comments.video = video
#             comments.save()
#             return redirect (to='videos', video_pk=video.video.pk)
#     return render (request, "video/add_comment.html", {'form':form, 'video':video})