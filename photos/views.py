from django.shortcuts import render, redirect
from .models import Category, Photo
import os
# from settings import PROJECT_ROOT

# Create your views here.

def home(request):
    return render(request, 'photos\home.html')


def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    

    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)



def viewPhoto(request, pk):
    photos = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photos': photos})



def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')


        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        
        
        photo = Photo.objects.create(
            category=category,
            description = data['description'],
            image = image,
        )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)



def editProduct(request, pk):
    photos = Photo.objects.get(id=pk)
    

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(photos.image) > 0:
                os.remove(photos.image.path)
            photos.image = request.FILES['image']
        photos.category = request.FILES['category']
        photos.description = request.FILES['description']
        photos.save()
        # messages.success(request, 'updated...')
        return redirect('gallery')


    context = {'photos': photos}
    return render(request, 'photos/edit.html', context)



def deleteProduct(request, pk):   
    photos = Photo.objects.get(id=pk)

    if len(photos.image) > 0:
        os.remove(photos.image.path)
    photos.delete()
    return redirect('gallery')
