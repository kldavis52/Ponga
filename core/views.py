from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required

# from .forms import  VideoForm, CommentsForm
from .models import User, Video, Comment
from .forms import InstructorForm, VideoForm, CommentsForm


def video_upload(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.creator = request.user
            video.save()
            return redirect("video_upload")
    form = VideoForm()
    return render(request, "studiopal/video_upload.html", {"form": form})


def video_detail(request, video_pk):
    video = Video.objects.get(id=video_pk)
    return render(request, "studiopal/video_detail.html", {"video":video,"video_pk":video_pk})


def landing_page(request):
    videos = Video.objects.all()
    return render(request, "studiopal/landing_page.html", {"videos": videos})


def add_instructor(request):
    if request.method == "POST":
        form = InstructorForm(request.POST)
        if form.is_valid():
            return redirect(to="homepage")
    form = InstructorForm()
    return render(request, "studiopal/add_instructor.html", {"form": form})


# def view_instructor(request, user_pk)


def homepage(request):
    return render(request, "studiopal/homepage.html")


def add_comment(request, video_pk):
    video = get_object_or_404(Video, pk = video_pk)
    if request.method == 'POST':
        form =VideoForm()
        form=CommentsForm(data = request.POST)
        if form. is_valid():
            comments = form.save(commit=False)
            comments.author = request.user
            comments.video = video
            comments.save()
            return redirect (to='video_detail', video_pk=video_pk)
    return render (request, "studiopal/video_detail.html", {'form':form, 'video':video})

