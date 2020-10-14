from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

# from .forms import  VideoForm, CommentsForm
from .models import User, Video, Comment
from .forms import InstructorForm, VideoForm


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


def landing_page(request):
    if request.user.is_authenticated:
        return render(request, "studiopal/landing_page.html")
    return render(request, "studiopal/landing_page.html")


# def add_instructor_info(request):
#     if request.method == "POST":
#         form = InstructorForm(data=request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.bio = request.user
#             form.save()
#             return redirect(to="homepage")
#     else:
#         form = InstructorForm()
#     return render(request, "studiopal/add_instructor_info.html", {"form": form})


# def view_instructor(request, user_pk)


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

def add_instructor_info(request, user_pk):
    user = get_object_or_404(User.objects.all(), pk=user_pk)
    if request.method == 'POST':
        form = InstructorForm(data=request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect(to='instructor_detail', user_pk=user.pk)
    else:
        form = InstructorForm(instance=user)
    return render(request, 'studiopal/add_instructor_info.html', {'form': form, 'user': user})

def instructor_detail(request, user_pk):
    user = get_object_or_404(User.objects.all(), pk=user_pk)
    return render(request, 'studiopal/instructor_detail.html', {'user': user})