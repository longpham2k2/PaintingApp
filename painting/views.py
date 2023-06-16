import os
from django.shortcuts import render, get_object_or_404,redirect
from .models import Painting
from .models import UserLikePainting
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import PaintingUploadForm
from django.db.models import Q
from django.conf import settings
# from .forms import PaintingSearchForm


def painting_list(request):
    paintings = Painting.objects.all()
    return render(request,'pages/painting_list.html',{'paintings':paintings})

def painting_detail(request,pk):
    painting = get_object_or_404(Painting,pk=pk)
    paintings = Painting.objects.all()
    likeNumber = UserLikePainting.objects.filter(painting_id = painting.id).count()
    isLiked = UserLikePainting.objects.filter(painting_id = painting.id, user_id = request.user.id)
    return render(request,'pages/paiting_detail.html',{'painting':painting, 'likeCount':likeNumber, 'paintings':paintings, 'isLiked':isLiked})

@login_required
@user_passes_test(lambda u: u.is_staff)
def create_painting(request):
    if request.method == 'POST':
        form = PaintingUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PaintingUploadForm()
    return render(request,'pages/upload.html',{'form':form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def update_painting(request, pk):
    instance = get_object_or_404(Painting, id=pk)
    if request.method == 'POST':
        form = PaintingUploadForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            image_path = os.path.join(settings.MEDIA_ROOT, instance.image.name)
            # print (image_path)
            if os.path.exists(image_path):
                os.remove(image_path)
            form.save()
            return redirect('list')
    else:
        form = PaintingUploadForm(instance=instance)
    return render(request,'pages/upload.html',{'form':form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_painting(request, pk):
    instance = get_object_or_404(Painting, id=pk)
    if request.method == 'POST':
        image_path = os.path.join(settings.MEDIA_ROOT, instance.image.name)
        # print (image_path)
        if os.path.exists(image_path):
            os.remove(image_path)
        instance.delete()
    return redirect('list')

@login_required
def like_painting(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            painting_id = pk
            user_id = request.user.id
            UserLikePainting.objects.get_or_create(painting_id = painting_id, user_id = user_id)
        return redirect('detail', pk=painting_id)
    else:
        return redirect('list')

@login_required
def unlike_painting(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            painting_id = pk
            user_id = request.user.id
            paintingToUnlike = UserLikePainting.objects.get(painting_id = painting_id, user_id = user_id)
            paintingToUnlike.delete()
        return redirect('detail', pk=painting_id)
    else:
        return redirect('list')

# def painting_search(request):
#     form = PaintingSearchForm(request.GET)
#     if form.is_valid():
#         query = form.cleaned_data['query']
#         name = form.cleaned_data['name']
#         if name:
#             paintings = Painting.objects.filter(
#                 name__icontains=query,
#                 name=name
#             )
#         else:
#             paintings = Painting.objects.filter(
#                 name__icontains=query
#             )
#         return render(request, 'pages/painting_search.html', {'paintings': paintings})
#     else:
#         return render(request, 'pages/painting_search.html')
#     form = PaintingSearchForm(request.GET)
def painting_search(request):
    # form = PaintingSearchForm(request.GET)
    if 'query' in request.GET:
        query = request.GET.get('query')
        # paintings = Painting.objects.filter(name__icontains = query)
        multiple_query = Q(Q(name__icontains=query) | Q(upload_date__icontains=query))
        paintings = Painting.objects.filter(multiple_query)
        return render(request, 'pages/painting_search.html', {'paintings': paintings})
    else:
        paintings = Painting.objects.all()
        context = {
            'paintings': paintings 
        }
    return render(request, 'pages/painting_search.html',context)
        
        
