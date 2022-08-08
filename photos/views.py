from django.shortcuts import render, redirect
from.models import Category, photo
# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    if category==None:
        photos = photo.objects.all()
    else:
        photos=photo.objects.filter(category__name=category)

    categories=Category.objects.all()
    # photos=photo.objects.all()

    context={'categories':categories, 'photos': photos}
    return render(request, 'photos/gallery.html',context)

def viewphoto(request, pk):
    photos = photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photos': photos})

def addphoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category= Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photos = photo.objects.create(category=category, description=data['description'], image=image,)
        return redirect('gallery')
    context = {'categories': categories}
    return render(request, 'photos/add.html', context)