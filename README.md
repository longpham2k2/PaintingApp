# fresh_shop
1. Tạo project Diango tên "paiting_app":
    1.1 Vào folder muốn lưu project -> cmd 
    1.2 Gõ lệnh: django-admin startproject painting_app
2. Tạo app tên "painting" trong project:
    1.1 Tại project painting_app -> terminal
    1.2 Gõ lệnh: python manage.py startapp painting
    1.3 painting_app ->settings.py -> thêm'painting',
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'painting',
    ]
3. Tạo model "Painting" trong app "painting" để lưu trữ thông tin của tranh vẽ (với các thuộc tính: tên, mô tả, hình ảnh, ngày upload)
    3.1 painting -> models.py 
    3.2 class Painting(models.Model):
        name = models.CharField(max_length=50)
        description = models.TextField()
        image = models.ImageField()
        upload_date = models.DateTimeField(auto_now_add=True)
4. Tạo form "PaintingForm" cho việc upload hình ảnh tranh vẽ
    4.1 panting -> new file "forms.py" -> forms.py
    4.2 thêm thư viện
        from django import forms 
        from .models import Painting
    4.3 tạo PaintingForm
        class PaintingForm(forms.ModelForm):
        class Meta:
            model = Painting
            fields = '__all__'
5. Tạo trang quản lý tranh vẽ cho admin bằng Django admin
    5.1 painting ->admin.py
    5.2 thêm thư viện:
            from .models import Painting
        gõ lệnh:
            admin.site.register(Painting)
6. Tạo views để hiển thị trang chủ với danh sách tranh vẽ và tranh vẽ chi tiết
    6.1 painting -> views.py
    6.2 thêm thư viện: 
        from django.shortcuts import render, get_object_or_404
        from .models import Painting
        Gõ lệnh:
        def painting_list(request):
        = Painting.objects.all()
        return render(request,'pages/painting_list.html',{'paintings':paintings})

        def painting_detail(request,pk):
            painting = get_object_or_404(Painting,pk=pk)
            paintings = Painting.objects.all()
            return render(request,'pages/paiting_detail.html',{'painting':painting, 'paintings':paintings})
    6.3: html,css,js cho painting_list.html, paiting_detail.html
    6.4: tạo tài khoản django admin
    6.5 tạo url trong urls.py
    painting_app ->urls.py 
    from django.contrib import admin
    from django.urls import path, include
    from django.conf.urls.static import static
    from django.conf import settings
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('painting/', include('painting.urls')),
    ]
7. Tạo trang upload hình ảnh tranh vẽ với quyền admin.
    7.1: Tạo form PaintingUploadForm:
        painting ->forms.py
        class PaintingUploadForm(forms.ModelForm):
        class Meta:
            model = Painting
            fields = ['name', 'description','image']
    7.2: tạo một view for upload tranh
        painting ->views.py
        Tạo thư viện:
            from django.contrib.auth.decorators import login_required, user_passes_test
            from django.shortcuts import render, redirect
            from .forms import PaintingUploadForm
        Gõ lệnh
            @login_required
            @user_passes_test(lambda u: u.is_staff)
            def upload_painting(request):
                if request.method == 'POST':
                    form = PaintingUploadForm(request.POST,request.FILES)
                    if form.is_valid():
                        form.save()
                        return redirect('list')
                else:
                    form = PaintingUploadForm()
                return render(request,'pages/upload.html',{'form':form})
    7.3: Tạo template cho trang upload
        - painting -> new folder "templates\pages" các file html,css sẽ được lưu vào folder này, 
        cái file css sẽ lưu vào folder mới "static"
        - upload.html 
            {% block content %}
                <div class="upload">
                    <div class="upload-a">
                        <h2>Upload a Painting</h2>
                        <form method="post" enctype="multipart/form-data" class="upload-content">
                        {% csrf_token %}
                        {{ form.as_p }}
                        <button type="submit">Save</button>
                        </form>
                    </div>
                </div>
            {% endblock %}
    7.4 thêm url cho trang upload trong urls.py
        painting ->urls.py
        from django.urls import path
        from . import views
        urlpatterns = [
        path('upload/', views.upload_painting, name='upload'),
        path('', views.painting_list,name='list'),
        path('detail/<int:pk>/',views.painting_detail,name='detail'),
        path('search/',views.painting_search,name='search')
        ]
    7.5 painting -> tạo folder mới media để lưu ảnh người dùng sẽ update lên 
        7.5.1: painting ->settings.py
            thêm 
            import os
            BASE_DIRR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            MEDIA_URL = 'media/'
            MEDIA_ROOT = os.path.join(BASE_DIRR,'media')
8. Tạo views để tìm kiếm theo ngày upload hoặc mô tả
    8.1 painting -> views.py
    8.2 gõ lệnh:
    Thêm thư viện:
    from django.db.models import Q

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
    

