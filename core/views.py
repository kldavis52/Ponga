from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# from .models import Video, Comment
# from .forms import  VideoForm, CommentsForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
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

